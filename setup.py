#!/usr/bin/env python

from setuptools import setup

# Version info -- read without importing
_locals = {}
with open('alabaster/_version.py') as fp:
    exec(fp.read(), None, _locals)
version = _locals['__version__']

setup(
    name='alabaster',
    version=version,
    description='A configurable sidebar-enabled Sphinx theme',
    author='Jeff Forcier',
    author_email='jeff@bitprophet.org',
    url='https://github.com/bitprophet/sphinx-theme',
    packages=['alabaster'],
    include_package_data=True,
    classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Topic :: Documentation',
          'Topic :: Software Development :: Documentation',
    ],
)
