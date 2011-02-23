#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Getopts template

When a script has many command line options, use this.

TODO: perhaps better way to handle global variables, options, etc

"""

# $Id$
__version__ = "$Rev$".split(': ')[1].split(' ')[0]

# standard library imports go here
import sys
import os
import traceback
import getopt

#import third party modules here

#import local application/library specific module here


class gb:
	"""Global Variables."""
	prefs = { 'verbose' : 0 }


def getPrefs():
	"""Parse the commandline options.
	
	Store options in the global 'gb.prefs' dict, and return the remaining 
	arguments.
	
	"""
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hv")
	except:
		print "Invalid options\n"
		usage()
		sys.exit(2)

	for o, a in opts:
		if o == '-h':
			gb.prefs['help'] = 1
		elif o == '-v':
			gb.prefs['verbose'] += 1
	return args


def log(msg, priority=1):
	"""Print the given message if the verbose level is high enough."""
	if gb.prefs['verbose'] >= priority:
		print >> sys.stderr, msg


def usage():
	"""Usage information (called with -h option)."""
	# uncomment the line below to print the module docstring (the top docstring)
	#print __doc__
	print "Usage:  %s" % os.path.basename(sys.argv[0])
	print ' -h  This help message'
	print ' -v  Verbosity, add more to be more verbose'


def main():
	"""The main function."""
	args = getPrefs()
	log("PREFS: %s" % gb.prefs)
	if "help" in gb.prefs:
		usage()
		sys.exit(2)
	# rest of program here
	print "hello world!"


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
