from setuptools import setup, find_packages
import subprocess
import sys
import shutil
import hapiDES



setup(
    name = "hapiDES",
    version = hapiDES.__version__,
    url = 'https://github.com/IamVNIE/hapi-des',
    license = 'All rights reserved.',
    author = "Vinayaka Jyothi.",
    author_email = "vj338@nyu.edu",
    packages = ['hapiDES'],
    package_data = {
 #   '' : ['*.bit','*.tcl','*.so'],
    '' : ['*.bit','*.tcl','*.py'],
    },
    description = "PYNQ DES ACCELERATOR OVERLAY"
)
