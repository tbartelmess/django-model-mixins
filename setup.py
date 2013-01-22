#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script
"""

from distutils.core import setup

setup(name='django-model-mixins',
      version='1.0.1',
      description='Simple helper to extend django models using mixins',
      author='Thomas Bartelmess',
      author_email='thomas.bartelmess@me.com',
      url='https://github.com/tbartelmess/django-model-mixins',
      packages=['modelmixins'],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
     ],
     )
