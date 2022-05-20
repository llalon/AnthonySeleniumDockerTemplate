#!/usr/bin/env python3

import os
import setuptools

readme = os.path.join(os.path.dirname(__file__), "README.md")
with open(readme, "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anthony",
    description="anthony",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="1.0",
    packages=["anthony"],
    license="anthony",
    author="anthony",
    author_email="anthony@anthony.anthony",
    url="anthony.com",
    install_requires=[
        "selenium",
        "selenium-requests",
        "requests",
    ],
    python_requires=">=3.6",
    entry_points=dict(
        console_scripts=[
            "anthony = anthony.cli:main",
        ],
    ),
)