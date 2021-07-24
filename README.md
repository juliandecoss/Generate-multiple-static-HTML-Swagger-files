# SWAGGER GENERATOR HTML FILES

This Repo creates beautiful html swagger files, using YAML files and validates them.


## Getting started

Make sure you have installed

- [Python 3.7+](https://www.python.org/downloads/)


## Installation

To install the libraries, run in your terminal.

```sh
make install
```

This will setup your environment to add the 2 libraries this repo requires.


## Adding your  YAML docs

In order to validate your files add your docs to the directory docs/openapi.


## Validating your yaml files

To validate your files first add them in the directory openapi, then run in your terminal:

```sh
make swagger-validation
```

## Creating your html beautiful swagger static docs
In order to connect your files between each one, change the file template in scripts/templates/swagger_template, you will find in the line 36 that there is a "select" html element, add all your files there, as options "<option value="name_of_your_file">name_of_your_file</option>" its not necessary to add the sufix html.

Once you finish this step just run in your terminal

```sh
make swagger-static
```


#### Credits to
This repo was built using the script shown below:
- https://gist.github.com/oseiskar/dbd51a3727fc96dcf5ed189fca491fb3