import datetime
import json

import click


@click.command()
@click.option(
    "--input-file",
    type=click.Path(exists=True),
    help="Path to the input file.",
    required=True,
)
@click.option("--include-city", is_flag=True, help="Include city information.")
@click.option("--write-output", is_flag=True, help="Write output to a text file.")
@click.option(
    "--output-file",
    type=click.Path(),
    default="./assets/output.txt",
    help="Output text file path.",
)
def cli(
    input_file: str, include_city: bool, write_output: bool, output_file: str
) -> None:
    """
    Process a JSON file containing user data and optionally include city
    information and write the output to a text file.
    Args:
        input_file (str): Path to the input JSON file.
        include_city (bool): Whether to include city information in the output.
        write_output (bool): Whether to write the output to a text file.
        output_file (str): Path to the output text file.
    """

    # NOTE - In a production scenario, you would want to add error handling,
    # input validation, and possibly logging. For the sake of simplicity,
    # these aspects are omitted here.

    # Load data from the input JSON file
    with open(input_file, "r") as f:
        records = json.load(f)["data"]

    # Process each record and generate output
    for record in records:
        output_string = "{name} is {age} years old.".format(**record)

        # Optionally include city information
        if include_city:
            output_string += " He lives in {city}.".format(**record)

        click.echo(output_string)
        click.echo("\n")

        # Optionally write output to a text file
        if write_output:
            with open(output_file, "a") as _output_file:
                _output_file.write(
                    "{}: {}\n".format(datetime.datetime.now(), output_string)
                )


if __name__ == "__main__":
    cli()
