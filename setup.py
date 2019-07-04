#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'py_project_base'
DESCRIPTION = 'A starting point for many python projects'
URL = ''
EMAIL = ''
AUTHOR = ''
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None
SETUP_REQUIREMENTS = ['pytest-runner', ]
TEST_REQUIREMENTS = ['pytest', ]
CLASSIFIERS = [
                  'Development Status :: 1 - Planning',
                  'Intended Audience :: Developers',
                  'Natural Language :: Russian',
                  'License :: Other/Proprietary License',
                  'Programming Language :: Python :: 3',
                  'Programming Language :: Python :: 3.6',
                  'Programming Language :: Python :: 3.7',
                  'Programming Language :: Python :: 3.8',
                  'Environment :: No Input/Output (Daemon)',
                  'Operating System :: POSIX :: Linux',
              ]
# What packages are required for this module to be executed?
REQUIRED = [
    'click',
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.rst')) as f:
        long_description = '\n' + f.read()
        long_description_mime = 'text/x-rst'
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


# Where the magic happens:
# noinspection SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type=long_description_mime,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    setup_requires=SETUP_REQUIREMENTS,
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='Other/Proprietary License',
    # Trove classifiers
    # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=CLASSIFIERS,
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
