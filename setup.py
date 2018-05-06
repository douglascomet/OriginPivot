#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from os.path import dirname
from os.path import join

from setuptools import setup
from setuptools import find_packages

import versioneer

requirements = []


test_requirements = [
    # TODO: put package test requirements here
]


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='OriginPivot',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Maya methods to manipulate pivots',
    license="MIT",
    author='Doug Halley',
    author_email='douglascomet@gmail.com',
    url='https://github.com/douglascomet/OriginPivot',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={},
    python_requires='',
    include_package_data=True,
    # Requirements
    install_requires=requirements,
    tests_require=test_requirements,
    zip_safe=False,
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    test_suite='tests',
)
