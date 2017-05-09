#!/usr/bin/env python

# Copyright (c) 2017, Cyril Gratecos <cyril.gratecos@gmail.com>
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.


from __future__ import print_function
import os, sys

setup_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(setup_dir, 'src'))


try:
    from setuptools import setup
    extra = dict(test_suite="tests.test.suite", include_package_data=True)
except ImportError:
    from distutils.core import setup
    extra = {}

from fcu_ansible import __version__

if sys.version_info <= (2, 5):
    error = "ERROR: fcu_ansible requires Python Version 2.6 or above...exiting."
    print(error, file=sys.stderr)
    sys.exit(1)

def readme():
    with open("README.md") as f:
        return f.read()

setup(name = "fcu_ansible",
      version = __version__,
      description = "Outscale Cloud Platform Ansible's Library",
      long_description = readme(),
      author = "Cyril Gratecos",
      author_email = "cyril.gratecos@gmail.com",
      #scripts = ["src/bin/ansible-fcu"],
      url = "https://github.com/delabale/fcu-ansible/",
      package_dir = {'': 'src'},
      #package_dir = {'toto': ''},
      packages = ["fcu_ansible"],
      #package_data = { "fcu_boto.cacerts": ["cacerts.txt"], "fcu_boto": ["endpoints.json"],
      #},
      license = "MIT",
      platforms = "Posix; MacOS X; Windows",
      classifiers = ["Development Status :: 5 - Production/Stable",
                     "Intended Audience :: Developers",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                     "Topic :: Internet",
                     "Programming Language :: Python :: 2",
                     "Programming Language :: Python :: 2.6",
                     "Programming Language :: Python :: 2.7",
                     "Programming Language :: Python :: 3",
                     "Programming Language :: Python :: 3.3",
                     "Programming Language :: Python :: 3.4"],
      **extra
      )
