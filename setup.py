import os, sys, subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install 

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

def pip_install(package_name):
    subprocess.call(
        [sys.executable, "-m", 'pip', 'install', package_name]
    )

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)

        # Install all required pip packages
        for p in parse_requirements('requirements.txt'):
            pip_install(p)
        
        # Downloads requisite packages after downloading 
        os.system("python -m spacy download en_core_web_sm")
        import nltk
        nltk.download('punkt')
        from sentence_transformers import SentenceTransformer
        embedder = SentenceTransformer('bert-base-nli-stsb-mean-tokens')

setup(
    name=NAME,
    version=VERSION,
    description='A python package for providing detailed analysis of apps and products from Amazon, Apple',
    long_description=read('README.md'),
    author='Vedant Sanil',
    author_email='vedantsanil@gmail.com',
    license='GNU LGPL 3',
    python_requires='>3.6',
    cmdclass={
        'install':PostInstallCommand,
    },
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