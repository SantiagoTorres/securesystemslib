#! /usr/bin/env python

"""
<Program Name>
  setup.py

<Author>
  Vladimir Diaz <vladimir.v.diaz@gmail.com>

<Started>
  December 7, 2016.

<Copyright>
  See LICENSE for licensing information.

<Purpose>
  BUILD SOURCE DISTRIBUTION

  The following shell command generates a TUF source archive that can be
  distributed to other users.  The packaged source is saved to the 'dist'
  folder in the current directory.

  $ python setup.py sdist


  INSTALLATION OPTIONS

  pip - installing and managing Python packages (recommended):

  # Installing from Python Package Index (https://pypi.python.org/pypi).
  $ pip install securesystemslib

  # Installing from local source archive.
  $ pip install <path to archive>

  # Or from the root directory of the unpacked archive.
  $ pip install .

  Alternate installation options:

  Navigate to the root directory of the unpacked archive and
  run one of the following shell commands:

  Install to the global site-packages directory.
  $ python setup.py install

  Install to the user site-packages directory.
  $ python setup.py install --user

  Install to a chosen directory.
  $ python setup.py install --home=<directory>


  Note: The last two installation options may require modification of
  Python's search path (i.e., 'sys.path') or updating an OS environment
  variable.  For example, installing to the user site-packages directory might
  result in the installation of TUF scripts to '~/.local/bin'.  The user may
  then be required to update his $PATH variable:
  $ export PATH=$PATH:~/.local/bin
"""

from setuptools import setup
from setuptools import find_packages


with open('README.rst') as file_object:
  long_description = file_object.read()

setup(
  name = 'securesystemslib',
  version = '0.10.8',
  description = 'A library that provides cryptographic and general-purpose routines for Secure Systems Lab projects at NYU',
  long_description = long_description,
  author = 'https://www.updateframework.com',
  author_email = 'theupdateframework@googlegroups.com',
  url = 'https://github.com/secure-systems-lab/securesystemslib',
  keywords = 'cryptography, keys, signatures, rsa, ed25519, ecdsa',
  classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: Freely Distributable',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Operating System :: POSIX :: Linux',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation :: CPython',
    'Topic :: Security',
    'Topic :: Software Development'
  ],
  install_requires = ['six>=1.11.0', 'cryptography>=2.1.3', 'pynacl>=1.2.0'],
  packages = find_packages(exclude=['tests']),
  scripts = []
)
