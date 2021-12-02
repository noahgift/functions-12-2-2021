#!/usr/bin/env python
import click
from logic import sentiment

@click.command()
@click.option(
    "--text",
    help="Type in a phrase to get the sentiment",
)
def make_sentiment(text):
    """Detects the emotion of a phrase"""

    result = sentiment(text)
    if 'NEGATIVE' in result:
        click.echo(click.style(f"{result}", fg="red"))
    else:
        click.echo(click.style(f"{result}", fg="green"))

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    make_sentiment()





