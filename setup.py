#!/usr/bin/env python

import codecs
from setuptools import setup

# Version info -- read without importing
_locals = {}
with open("alabaster/_version.py") as fp:
    exec(fp.read(), None, _locals)
version = _locals["__version__"]

# README into long description
with codecs.open("README.rst", encoding="utf-8") as f:
    readme = f.read()

code_ns = "bitprophet/alabaster"

setup(
    name="alabaster",
    version=version,
    description="A configurable sidebar-enabled Sphinx theme",
    long_description=readme,
    author="Jeff Forcier",
    author_email="jeff@bitprophet.org",
    url="https://alabaster.readthedocs.io",
    project_urls={
        "Source": f"https://github.com/{code_ns}",
        "Changelog": f"https://github.com/{code_ns}/blob/main/docs/changelog.rst",  # noqa
        "CI": f"https://app.circleci.com/pipelines/github/{code_ns}",
    },
    packages=["alabaster"],
    include_package_data=True,
    entry_points={"sphinx.html_themes": ["alabaster = alabaster"]},
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
)
