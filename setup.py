import os
from setuptools import setup, find_packages

from reviewanalysis import __VERSION__

NAME = 'reviewanalysis'
VERSION = __VERSION__

def read(filename):
    """Readlines of filename relative to setup file path."""
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

def parse_requirements(filename):
    """Parses requirements.txt file"""
    ls = []
    with open(filename, "r") as f:
        for lines in f:
            ls.append(lines)

    return ls

setup(
    name=NAME,
    version=VERSION,
    description='A python package for providing detailed analysis of apps and products from Amazon, Apple',
    long_description=read('readme.md'),
    author='Vedant Sanil',
    author_email='vedantsanil@gmail.com',
    license='GNU LGPL 3',
    install_requires = parse_requirements('requirements.txt'),
    python_requires='>3.6',
    packages=find_packages(),
    url='https://github.com/vedant-sanil/reviewanalysis',
    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
    ],
)