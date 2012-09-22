#!/usr/bin/env python

from distutils.core import setup

setup(name = 'skeleton',
      version = '0.0',
      description = 'A python skeleton project',
      long_description = '''
This project represents a basic python skeleton project that can be used as
the basis for other projects.  Feel free to fork this project and use as you
see fit, but please update the information here.

Note: Licensing only applies to the skeleton itself, should you use this
      skeleton as the basis for a new project, update the license accordingly.
''',
      author = 'Chris Salch',
      author_email = 'emeraldd.chris@gmail.com',
      url = 'https://github.com/arlaneenalra/python-skeleton',
      classifiers = [
        'License :: OSI Approved :: BSD License'
      ],
      license = 'License :: OSI Approved :: BSD License',
      packages = [],
      scripts = [],
      py_modules = [],
      package_dir = { '': 'lib'},
)

