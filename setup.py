#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup

version = {}
with open("archaic_match/version.py") as fp:
    exec(fp.read(), version)

setup(
    name='archaic_match',
    version=version['__version__'],
    packages=['archaic_match'],
    entry_points={
        'console_scripts': [
            'archaic_match=archaic_match.__main__:main',
            'column_replace=archaic_match.column_replace:main'
        ]
    },
    install_requires=[
        'numpy',
        'matplotlib',
        # 'seaborn',
        # 'pandas',
        # 'h5py!=2.7.0,!=2.7.1',  # These versions issue warnings when imported
        'scikit-allel>=1.1.10'
    ]
)
