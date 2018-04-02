# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

import os
import re

package = 'python_aisweb'
init_py = open(os.path.join(package, '__init__.py')).read()
version = re.search(
    "^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)
author = re.search(
    "^__author__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)
email = re.search(
        "^__email__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)

try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    readme = ''


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='python-aisweb',
    packages=find_packages(),
    version=version,
    description='API Wrapper for brazilian AIS services.',
    long_description=readme,
    author=author,
    author_email=email,
    url='https://github.com/carlosdamazio/python-aisweb',
    install_requires=requirements,
    license="MIT",
    keywords=['dev', 'api', 'aisweb', 'aeronautics'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
