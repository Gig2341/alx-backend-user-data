# Project Description

This project involves the development of a Python application that interacts with a database using SQLAlchemy 1.3.x and includes a Flask app for authentication (Auth) purposes. The project adheres to specific coding and documentation standards, and it uses the bcrypt library for password hashing.

## Environment and Execution

- The project is designed to be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- The allowed editors for working on the project are vi, vim, and emacs.
- All files in the project should end with a new line.
- The first line of every file must be `#!/usr/bin/env python3`.
- All files must be executable.

## Coding Style

- The project follows the pycodestyle style (version 2.5) for code formatting.
- Length of files will be tested using the `wc` command.

## Project Structure

- The project must include a `README.md` file at the root of the folder, providing documentation and information about the project.
- All modules, classes, and functions should have proper documentation.
- Documentation is expected to be more than a simple word; it should be a meaningful sentence explaining the purpose of the module, class, or method.
- Classes and functions must be type-annotated for clarity.

## Dependencies

- The project requires the installation of the `bcrypt` library, which can be installed using the command: `pip3 install bcrypt`.

## Flask App and Database Interaction

- The Flask app should interact only with the Auth module and should never communicate directly with the database (DB).
- Public methods of Auth and DB classes should be the only ones used outside these classes, ensuring a clear separation of concerns.

## Verification and Testing

- The length of files and adherence to documentation standards will be verified.
- The project will be tested using the specified Python version (3.7).
