from setuptools import setup, find_packages

setup(
    name='tip',
    version='0.1',
    description='Code to prepare traditional technical interviews.',
    url='https://github.com/davidgasquez/tip',
    author='David Gasquez',
    author_email='davidgasquez@gmail.com',
    license='Unlicense',
    packages=find_packages(),
    zip_safe=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
    ],
    keywords='algorithms data-structures'
)
