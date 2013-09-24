#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Python Template.

This is a template for python.
NOTE: The __future__ imports that make it more v3.x ready were added in v2.6.
Thus this template will only work in python v2.6 or higher.

"""

from __future__ import absolute_import, print_function, unicode_literals
import os
import sys
import traceback
import logging
from collections import OrderedDict

import gw2api


__version__ = 'alpha'


loglevel = getattr(logging, os.getenv('LOGLEVEL', 'WARNING').upper())
logformat = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
logging.basicConfig(level=loglevel, format=logformat)
log = logging.getLogger()

# know what these values should be without lookup
# tarnished coast world
world_id = '1017'
# bloodtide coast map
map_id = '73'

# Events I'm insterested in (specify them in order):
event_names = OrderedDict()
event_names['E5B1EF7A-DF6B-48A8-9EFD-5C40DFD270EB'] = (
            'Defend Lionguard Lindi as she searches for buried treasure.')
event_names['6158E720-41CB-4684-8F4A-86D2D122DF4D'] = (
            'Protect Bill and Hekja as they clear Risen from the area.')
event_names['B6B7EE2A-AD6E-451B-9FE5-D5B0AD125BB2'] = (
            'Eliminate the cannons at the northern defensive tower.')
event_names['189E7ABE-1413-4F47-858E-4612D40BF711'] = (
            "Capture Taidha Covington's southern defensive tower.")
event_names['0E0801AF-28CF-4FF7-8064-BB2F4A816D23'] = (
            "Defend the galleon and help it destroy Taidha's gate.")
event_names['242BD241-E360-48F1-A8D9-57180E146789'] = (
            'Kill Admiral Taidha Covington.')

log.debug('Requesting events for world %s, map %s' % (world_id, map_id))
events = gw2api.get_events(world_id=world_id, map_id=map_id)['events']

log.debug('Searching for values of events')
for k in event_names.keys():
    event = [item for item in events if item['event_id'] == k]
    print("%-11s %s" % (event[0]['state'], event_names[k]))
