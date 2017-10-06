#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
from setuptools import setup

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="affine6p",
    version="0.0.1",
    description="To calculate affine transformation parameters with six free parameters.",
    long_description=long_description,
    author="Masahiro Yoshimoto",
    author_email="yoshimoto@flab.phys.nagoya-u.ac.jp",
    url="https://gitlab.com/yoshimoto/affine6d",
    py_modules=["affine6p"],
    include_package_data=True,
    install_requires=["Flask"],
    tests_require=["nose"],
    license="MIT",
    keywords="calculate affine transformation six parameters",
    zip_safe=False,
    classifiers=[]
)