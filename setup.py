#!/usr/bin/env python3

from distutils.core import setup

setup(name='Wilcox',
      version='0.1.0',
      description='A rendering library for the conic sections of a curious geometry.',
      install_requires=['numpy', 'matplotlib.pyplot', 'tqdm'],
      author='Samuel Buckley-Bonanno',
      url='https://github.com/sbuckleybonanno/Wilcox',
      packages=['wilcox'],
     )
