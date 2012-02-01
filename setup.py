from distutils.core import setup

setup (name = 'hash-ring',
                version = '1.0',
                description = 'C implementation of ketama hashing',
                package_dir = {'': 'hash-ring/lib/python'},
                py_modules = ['chashring'])