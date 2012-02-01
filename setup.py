from distutils.core import setup
import subprocess

subprocess.call(["git", 'submodule', 'init'])
subprocess.call(["git", 'submodule', 'update'])

setup (name = 'chashring',
                version = '1.0',
                description = 'C implementation of ketama hashing',
                package_dir = {'': 'hash-ring/lib/python'},
                py_modules = ['chashring'])