#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RestApiCall",
    version="0.0.1",
    author="Olivier Locard",
    description="This python library is a REST API Call which generates REST URLs using attributes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/olo-dw/restapicall.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License"
    ],
)