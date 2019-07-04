#!/usr/bin/python
# vim: set fileencoding=utf-8 :

"""Main module."""
import sys
from typing import Any

import click


@click.command()
def main(args: Any = None) -> int:
    """Console script."""
    del args

    result_code = 0
    click.echo("Tabula rasa")
    return result_code


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
