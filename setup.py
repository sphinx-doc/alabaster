#!/usr/bin/env python

from setuptools import setup

# Version info -- read without importing
_locals = {}
with open('alabaster/_version.py') as fp:
    exec(fp.read(), None, _locals)
version = _locals['__version__']

# README into long description
with open('README.rst') as f:
    readme = f.read()

setup(
    name='alabaster',
    version=version,
    description='A configurable sidebar-enabled Sphinx theme',
    long_description=readme,
    author='Jeff Forcier',
    author_email='jeff@bitprophet.org',
    url='https://github.com/bitprophet/alabaster',
    packages=['alabaster'],
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
