import os
import sys
from pathlib import Path
from traceback import print_exc
from typing import Tuple

import click
from openapi_spec_validator import all_urls_handler, validate_spec
from openapi_spec_validator.exceptions import ValidationError


def validate_openapi_file(files) -> None:
    for file in files:
        spec_url = Path(file).as_uri()
        try:
            spec_dict = all_urls_handler(spec_url)
        except Exception:
            print(f"\n❌ Sintax error in file: {file}")
            print_exc(0)
            sys.exit(-1)
        try:
            validate_spec(spec_dict, spec_url=spec_url)
        except ValidationError:
            print_exc(0)
            print(f"\n❌ File: {file} does not match OpenApi 3.0 specs")
            sys.exit(-1)
        except:
            print_exc(0)
            sys.exit(-1)
    return


@click.command()
@click.argument(
    "src",
    nargs=-1,
    type=click.Path(exists=True, file_okay=True, dir_okay=True, readable=True),
    is_eager=True,
)
def main(src: Tuple[str, ...]) -> None:
    """Main. Uses openapi_spec_validator code to perform validation"""
    print("\nChecking documentation files...")
    directory = src[0]
    yml_files = os.listdir(directory)
    files = []
    absolute_path = str(Path(directory).resolve())
    for yml in yml_files:
        files.append(absolute_path + "/" + yml)
    if not files:
        print("❌ No files to validate")
        sys.exit(-1)
    validate_openapi_file(files)
    print("✅ Documentation matches OpenApi 3.0 specs\n")


if __name__ == "__main__":
    main()
