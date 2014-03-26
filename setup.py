# -*- coding: utf-8 -*-
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
    requires = f.read().splitlines()

setup(
    name="Adept",
    version="0.0.2",
    author="Fictive Kin",
    maintainer="Phil Howell",
    author_email="phil@fictivekin.com",
    description="Simple binding for Adept",
    license="MIT",
    install_requires=requires,
    keywords=['adept', 'image', 'resize', 'processing'],
    url="https://github.com/fictivekin/adept-python",
    download_url="https://github.com/fictivekin/adept-python/archive/0.0.2.tar.gz",
    packages=['adept'],
    package_data={'': ['LICENSE', 'README.md', 'requirements.txt']},
    include_package_data=True,
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
