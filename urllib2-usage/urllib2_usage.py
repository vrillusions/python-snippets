#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic example for using urllib2 to get a url

Big fan of requests module but if something is simple enough can just use the
built in urllib modules.

"""
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import sys
import urllib2
import json
import pprint
import logging


LOG = logging.getLogger()


def get_url(url):
    try:
        result = urllib2.urlopen(url).read()
    except urllib2.HTTPError as exc:
        LOG.error("HTTP Error: %s %s" % ( str(exc.code), str(exc.reason) ))
        return False
    except urllib2.URLError as exc:
        LOG.error("URL Error: %s" % str(exc))
        return False
    return result


def main():
    LOG.info("fetching url http://example.com")
    print(get_url('http://example.com/'))
    print()
    # what happens with a 404 error
    LOG.info("fetching url http://example.com/some-nonexistent-page")
    print(get_url('http://example.com/some-nonexistent-page'))
    print()
    # example to parse json results
    LOG.info("fetching url and then parse json response")
    content = json.loads(get_url('https://api.github.com/users/octocat'))
    pprint.pprint(content)


if __name__ == "__main__":
    _logformat = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=_logformat)
    sys.exit(main())

