#!/usr/bin/env python

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='question_generation',
    version='1.0.1',
    description='Question Generation using Transformers',
    long_description=read("README.md"),
    python_requires='>=2.7',
    license="MIT",
    packages=['question_generation'],

)

