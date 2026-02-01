import click
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


@click.command()
@click.option("--host", default="localhost", help="Database host.")
@click.option("--port", default=5432, help="Database port.")
@click.option("--user", default="user", help="Database user.")
@click.option("--password", default="password", help="Database password.")
@click.option("--dbname", default="mydb", help="Database name.")
def cli(host: str, port: int, user: str, password: str, dbname: str) -> None:
    """
    Connect to a PostgreSQL database using the provided connection parameters.

    Args:
        host (str): The database host. Defaults to "localhost".
        port (int): The database port. Defaults to 5432.
        user (str): The database user. Defaults to "user".
        password (str): The database password. Defaults to "password".
        dbname (str): The database name. Defaults to "mydb".
    """

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

    with engine.connect() as connection:
        with Session(connection) as session:
            result = session.execute("SELECT version();")
            version = result.fetchone()
            click.echo(f"Connected to database. PostgreSQL version: {version[0]}")


if __name__ == "__main__":
    cli()
