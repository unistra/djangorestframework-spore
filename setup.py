# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='drf-spore',
    version='0.1.0',
    description='drf addon for Spore specification',
    long_description=readme,
    author='Arnaud Grausem'
    author_email='arnaud.grausem@unistra.fr',
    url='https://github.com/unistra/djangorestframework-spore',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

