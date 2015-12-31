#!/usr/bin/env python
# -*- coding: utf-8 -*-

__company__ 	= 'Sequømics Corporation'
__homepage__ 	= 'http://sequomics.com/'
__account__ 	= 'SequomicsCorporation'
__githubURL__ 	= 'https://github.com/SequomicsCorporation'
__authors__ 	= [
    '"Prabhat Kumar" <prabhat.genome@gmail.com>',
    '"Sequømics Corporation" <admin@sequomics.com>'
    ]
__license__     = 'Apache License'

# ------------------------------------------------------------------------
# Copyright © 2014 - 2015, Sequømics Corporation. All rights reserved.
#
# Licensed under the Apache License, Version 2.0, (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#       	http://www.apache.org/licenses/LICENSE-2.0
#                           	or
#       https://github.com/ANKdb/ANKdb/blob/master/LICENSE
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
# ================================= ANKdb® ===============================
import os
import sys
import platform
import errno
from os import sep as dirsep
from os.path import isfile, join

from distutils.core import setup
from distutils.extension import Extension
from distutils.command.install import install

# A:1 - Python Version Information.
if sys.version_info[:2] < (2, 6):
    sys.stderr.write('ANKdb®: Python 2.5 and older is not supported!\n')
    sys.exit()

# A:2 - JavaOS Support Information.
if os.name == 'java':
    sys.stderr.write('ANKdb®: JavaOS is not supported!\n')
    sys.exit()

# A:3 - NumPy Support Information.
try:
    import numpy
except ImportError:
    sys.stderr.write('ANKdb®: numpy is not installed, you can find it at: '
                     'http://numpy.scipy.org/\n')
    sys.exit()

if [int(dgt) for dgt in numpy.__version__.split('.')[:2]] < [1, 4]:
	sys.stderr.write('ANKdb®: numpy v1.4 or later is required, you can find it at: '
                     'http://numpy.scipy.org/\n')
	sys.exit()

# A:4 - SciPy Support Information.
try:
    import scipy
except ImportError:
    sys.stderr.write('ANKdb®: scipy is not installed, you can find it at: '
                     'http://www.scipy.org/\n')
    sys.exit()

if [int(dgt) for dgt in scipy.__version__.split('.')[:2]] < [0, 4]:
    sys.stderr.write('ANKdb®: scipy v0.14 or later is required, you can find it at: '
                     'http://www.scipy.org/\n')
    sys.exit()

# ================================= ANKdb® ===============================
# A:5 - ANKdb® Information.
__version__ 	= '1.0.0'

with open('ankdb/__init__.py') as inp:
    for line in inp:
        if line.startswith('__version__'):
            exec(line.strip())
            break

with open('docs/README.rst') as inp:
    long_description = inp.read()
