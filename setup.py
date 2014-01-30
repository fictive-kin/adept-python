# -*- coding: utf-8 -*-
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="adept",
    version="0.0.1",
    author="Fictive Kin",
    author_email="phil@fictivekin.com",
    description="Simple binding for Adept",
    license="BSD",
    install_requires=required,
    keywords="adept image processing",
    url="https://github.com/fictivekin/adept-python",
    packages=['adept', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)