from setuptools import setup, find_packages
import subprocess
import sys
import shutil
import hapiv1



setup(
    name = "hapiDES",
    version = hapides.__version__,
    url = 'https://github.com/IamVNIE/hapi-dev',
    license = 'All rights reserved.',
    author = "Vinayaka Jyothi.",
    author_email = "vj338@nyu.edu",
    packages = ['hapiDES'],
    package_data = {
 #   '' : ['*.bit','*.tcl','*.so'],
    '' : ['*.bit','*.tcl','*.so','*.py'],
    },
    description = "PYNQ DES ACCELERATOR OVERLAY"
)
