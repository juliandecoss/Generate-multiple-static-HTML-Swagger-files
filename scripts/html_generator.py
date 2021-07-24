from pathlib import Path
from openapi_spec_validator import all_urls_handler
import json
from templates.swagger_template import TEMPLATE
import click
from typing import Tuple
import os

def create_static_file(file):
  spec_url = Path(file).as_uri()
  spec = all_urls_handler(spec_url)
  name_file = file.split("/")
  name_file = "./docs/static/"+name_file[len(name_file)-1].replace("yml","html")
  file = open(name_file,"w")
  file.write(TEMPLATE % json.dumps(spec))
  file.close()


def create_directory(parent_dir:str)->str:
    directory_name = "static"
    absolute_path = str(Path(parent_dir).resolve()).replace("openapi",directory_name)
    try:
      os.mkdir(absolute_path)
    except:
      print(" 📁 Directory was already created 📁\n")
    return absolute_path

@click.command()
@click.argument(
    "src",
    nargs=-1,
    type=click.Path(exists=True, file_okay=True, dir_okay=True, readable=True),
    is_eager=True,
)
def main(src: Tuple[str, ...]) -> None:
    print("🏁 Starting static files creation 🏁\n")
    print("Checking documentation files...\n")
    parent_dir = src[0]
    directory_path = create_directory(parent_dir)
    yml_files = os.listdir(parent_dir)
    absolute_yml_path = str(Path(parent_dir).resolve())
    files = []
    for yml in yml_files:
        files.append(absolute_yml_path + "/" + yml)
    for file in files:
      create_static_file(file)
    print(" ALL THE STATIC FILES 📝 HAVE BEEN CREATED 🖌 IN THE DIRECTORY <docs/static>\n")

if __name__ == "__main__":
    main()
