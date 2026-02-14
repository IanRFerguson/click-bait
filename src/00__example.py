import click


@click.command()
@click.option("--name", default="partner", help="The person to greet.")
def cli(name: str) -> None:
    """Simple program that greets NAME."""

    # NOTE: We use click.echo instead of print for better compatibility
    # across different environments / operating systems. This isn't
    # stricly necessary, if you're only developing tools for yourself
    # or your internal team, but it's a good practice to get into.
    click.echo(f"Howdy, {name}! Thanks for reading.")
    click.echo("\n")


if __name__ == "__main__":
    cli()
