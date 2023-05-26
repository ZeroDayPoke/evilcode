#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='package_demo',
    version='0.1',
    packages=find_packages(),
    description='A simple example package',
    author='Chris Stamper',
    author_email='cstampok@gmail.com',
    url='https://github.com/ZeroDayPoke/evilcode/console/package_demo',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10.6',
    ],
)
