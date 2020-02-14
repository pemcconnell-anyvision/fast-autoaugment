#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    raise RuntimeError("automation-infra requires Python 3.6+")

with open('README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

with open('requirements.txt', mode='r', encoding='utf-8') as f:
    install_requires = f.read().splitlines()

setup(
    name='fast-autoaugment',
    author='kakaobrain',
    maintainer='peter mcconnell',
    description='see readme',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.6',
    install_requires=install_requires,
)
