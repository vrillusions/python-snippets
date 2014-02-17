#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Caching.

Couple examples on caching data.

"""

from __future__ import absolute_import, print_function, unicode_literals, division
import os
import sys


our_data = {
    'id': 1234,
    'name': 'John Doe',
    'email': 'jdoe@example.com',
    }

# Use cPickle for smaller datasets and also when you'll need access to most of
# the values stored in it. cPickle always loads the entire contents into memory.
#import cPickle as pickle
import pickle

# Note that it's open as binary. This should be done even if storing as protocol
# 0 which is ascii
with open('cache.db', 'wb') as fh:
    # The -1 means to use the highest protocol available. Which in most cases is
    # whate you want. For debugging it may be useful to have this set to
    # protocol 0 which stores the information in an easier to read plain text
    # format. If a number isn't specified then will default to 0
    pickle.dump(our_data, fh, -1)

# To get data back
with open('cache.db', 'rb') as fh:
    cached_data = pickle.load(fh)


# Use shelve for larger datasets. This stores the contents in a file based
# database like bdb but could be one of several different formats. One important
# distinction is shelve keeps the file handle open the entire session while
# pickle only accesses the file to read or write the data.
import shelve

# setting writeback=True causes the entire file to read into memory. This is
# needed when altering a value (something like dict.append()) as python doesn't
# know if a value has been changed unless the new value is assigned to that key.
# The default is False, just specified here as an example. If you're using this
# for a large dataset than you should make sure writeback is False and when
# updating values always explicitly assign the new value. Protocol has the same
# meaning as pickle since that's what it is used for.
#
# This is an unsafe implementation of this. If any error happens it could cause
# the database to not close properly and corrupt it. So don't copy and paste
# this part of the code.
#
# note that python may optionally add it's own extension to this
persistent_data = shelve.open('cache2', protocol=-1, writeback=False)

# NOTE: because of the unicode_litterals import need to specify indexes as byte
# strings or else it will get treated as unicode and cause an AttributeError
#
# Without writeback=True this will work
persistent_data[b'XX'] = [0, 1, 2]
# But this will not (will still have range(4))
persistent_data[b'XX'].append(3)

# If you find yourself doing a lot of mutations like this then you can either
# fix it to not do that or set writeback=True

# Make sure to close the file afterwards
persistent_data.close()
