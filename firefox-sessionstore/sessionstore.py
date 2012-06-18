#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Lists all the URLs in a firefox sessionstore file"""
import json

fp = open('sessionstore.js', 'r')
data = json.load(fp)

#print json.dumps(data, indent=4)
for win in data['windows']:
    for tab in win['tabs']:
        print tab['entries'][0]['url']
