# Environment Controller

`EnvironmentController` is a Python class designed to manage environment variables for your application. It provides a simple and efficient way to parse and handle environment variables from a `.env` file.

## Features

- **Easy Parsing**: The `parse_env_file` method reads an environment file and returns a dictionary of the environment variables. It handles comments and empty lines gracefully, and warns about lines that don't follow the expected format.

- **Flexible**: It's designed to be used in any Python application that needs to manage environment variables.

- **Error Handling**: It provides clear error messages for lines in the `.env` file that don't follow the expected `KEY=VALUE` format.

Remember to always keep your `.env` file out of version control to avoid exposing sensitive information.

## Installation

You can install the package using pip:


pip install py_env_parser

# Usage

from py_env_parser import EnvironmentController

## Create an instance of the controller
controller = EnvironmentController()

## Parse the .env file
env_vars = controller.parse_env_file('.env')

## Now you can access your environment variables
print(env_vars['MY_VARIABLE'])
