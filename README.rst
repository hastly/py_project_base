.. |copy|    unicode:: U+000A9 .. COPYRIGHT SIGN
.. |check|   unicode:: U+02714 .. HEAVY CHECK MARK
.. |uncheck| unicode:: U+02261 .. IDENTICAL TO

#############
PyProjectBase
#############

Starting point for generic python project


Features
********

* basic project structure and description
* initial python package setup
* python environment
* testing and linting development packages
* versioning ignore setup
* editor config


Steps
*****

|check| create project directory and start this file with description and "steps" section

    #. README.rst (this file)

|check| create to be versioned git ignore alternatives (with IDE settings versioning and wo them):

    #. .gitignore.with.ide
    #. .gitignore.wo.ide

    https://www.gitignore.io/api/python,intellij,vim,code,linux,windows

|check| init repo and copy one of ignore alternatives as unversioned

|check| compose editor setup file

    #. .editorconfig

|check| generate pipenv environment in project directory (export PIPENV_VENV_IN_PROJECT=1)

|check| install development toolkit into local environment :

    #. Pipfile

.. code-block::

    [dev-packages]
    pytest = "*"
    pytest-mock = "*"
    pytest-runner = "*"
    pytest-asyncio = "*"
    tox = "*"
    tox-pipenv = "*"
    coverage = "*"
    flake8 = "*"
    mypy = "*"
    bump2version = "*"

    [packages]
    click = "*"

|check| create starting entry point and starting test

    #. py_project_base_src/cli.py
    #. tests/test_cli.py

|check| create requirements files from pipenv

    pipenv lock -r [--dev] > ...

|check| create IDEA project from this directory and setup run/test configurations

|check| create setup.{py,cfg} and fill them with app info:

    #. setup.py
    #. setup.cfg

    https://github.com/kennethreitz/setup.py

|check| configure version scheme, set initial version in app/__version__.py

    #. __version__.py
    #. bump.sh

|check| add to ignore
    
    #. .gitignore

|check| commit that as an inception point, bump version


Changelog
*********

    - init repo together with ignore options
    - setup editor config and init IDEA
    - add starting development dependencies
    - configure version bump
    - compose python package setup files
    - add starting entry point and test
    - add starting readme


Personal bits
*************

#. -*- README.rst -*-

    - set name and credits
    - compose own description
    - add features and steps
    - etc.

#. -*- setup.py -*-

    - edit personal info in the beginning
