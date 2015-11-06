#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Very basic implementation to create a SSHA password."""
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import hashlib
import base64
import getpass
import os


password = getpass.getpass('Enter password to hash: ')
salt = raw_input('Enter salt in hex or hit enter to generate one: ')
if salt:
    salt = salt.decode('hex')
else:
    salt = os.urandom(8).encode
print(salt)
print('{SSHA}' + hashlib.sha1(password + salt).hexdigest() + salt.encode('hex'))
