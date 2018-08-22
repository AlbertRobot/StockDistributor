# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='StockDistributor',
    version='1.0.0',
    description='Mock stock distributor',
    long_description=readme,
    author='Kenneth Reitz',
    author_email='sjtuzhaoxh@gmail.com',
    packages=find_packages(exclude=('tests', 'docs'))
)

