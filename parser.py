
import click
from models import Parser



def process_file(filename:str) -> str:
    
    parser = Parser()
    parser.parse_file(filename)
    return parser.to_json()
    
@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option(
    "-out",
    "--output",
    "output",
    type=click.Path(writable=True),
    help="File to write the parsed JSON output.",
)

def main(file: str, output):
    """Parse a CSV file to EventLog data and output grouped JSON"""

    click.echo(f"Parsing file: {file}")
    json_data = process_file(file)

    
    if output:
        with open(output, "w", encoding="utf-8") as fp:
            fp.write(json_data)
        click.echo(f"JSON ouptut written to {output}")
    else:
        click.echo(json_data)


if __name__ == "__main__":
    main()