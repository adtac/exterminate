import codecs
import setuptools
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='destruction',

    version='0.1.0',

    description='Destroy Python programs with a simple import.',

    url='https://github.com/adtac/destruction',

    author='Adhityaa Chandrasekar',
    author_email='c.adhityaa@gmail.com',

    license='MIT',

    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    packages=['destruction'],
)
