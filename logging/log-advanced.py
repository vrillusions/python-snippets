#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Advanced logging template.

This is an example of using the logging function.

This shows how to create a custom format

If you are to this point it may be better to use a config file for logging
see: http://docs.python.org/library/logging.html#configuring-logging

"""

import sys
import os
import traceback
import logging

class SomeClass:
    def __init__(self):
        self._log = logging.getLogger('%s.%s' % (__name__, self.__class__.__name__))
    
    def error(self):
        self._log.warning('test warning message')

def main():
	"""The main function."""
	# Default format doesn't include a timestamp
	# This also shows how you specify a console handler, setup is similar for
	# a file handler
	log = logging.getLogger(__name__)
	log.setLevel(logging.WARNING)
	# create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    log.addHandler(ch)
	log.warning('test warning message')
	sc = SomeClass()
	sc.error()


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt, e:
		# Ctrl-c
		raise e
	except SystemExit, e:
		# sys.exit()
		raise e
	except Exception, e:
		print "ERROR, UNEXPECTED EXCEPTION"
		print str(e)
		traceback.print_exc()
		sys.exit(1)
	else:
		# Main function is done, exit cleanly
		sys.exit(0)