import codecs
import setuptools
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

setuptools.setup(
    name='exterminate',

    version='0.2.0',

    description='Break Python programs with a simple import.',

    url='https://github.com/adtac/exterminate',

    author='Adhityaa Chandrasekar',
    author_email='c.adhityaa@gmail.com',

    install_requires=open("requirements.txt").read().splitlines(),

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

    packages=['exterminate'],
)
