import click
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


@click.command()
@click.option("--host", help="Database host.", required=True)
@click.option("--port", help="Database port.", required=True)
@click.option("--user", help="Database user.", required=True)
@click.option("--password", help="Database password.", required=True)
@click.option("--dbname", help="Database name.", required=True)
def cli(host: str, port: int, user: str, password: str, dbname: str) -> None:
    """
    Connect to a PostgreSQL database using the provided connection parameters.

    Args:
        host (str): The database host.
        port (int): The database port.
        user (str): The database user.
        password (str): The database password.
        dbname (str): The database name.
    """

    # Format connection string and create SQLAlchemy engine
    connection_string = (
        "postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(
            user=user,
            password=password,
            host=host,
            port=port,
            dbname=dbname,
        )
    )
    engine = create_engine(connection_string)

    # Test connection and print Postgres version to the terminal
    with engine.connect() as connection:
        with Session(connection) as session:
            result = session.execute(text("SELECT version();"))
            version = result.fetchone()
            click.echo(
                f"\n* Connected to database {host}:{port}/{dbname} as user {user}"
            )
            click.echo(f"\n* Database version: {version[0]}\n")


if __name__ == "__main__":
    cli()
