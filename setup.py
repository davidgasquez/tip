import io
from setuptools import setup


def README():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(
    name='tip',
    version='0.1',
    description='Code to prepare traditional technical interviews.',
    long_description=README(),
    url='https://github.com/davidgasquez/tip',
    author='David Gasquez',
    author_email='davidgasquez@gmail.com',
    license='Unlicense',
    packages=['tip'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
    ],
    keywords='algorithms data-structures'
)
