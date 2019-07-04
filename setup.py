"""setup.py
"""
from setuptools import setup, find_packages

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='htmler',
    version='0.1',
    author='Oleksandr Shepetko',
    author_email='a@shepetko.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashep/htmler",
    packages=find_packages(),
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov'],
)
