#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Minimal template.

This is useful when the script doesn't take many options

"""

# $Id$
__version__ = "$Rev$".split(': ')[1].split(' ')[0]

import sys
import os
import traceback


def usage():
    """Usage information (called with -h option)."""
    # uncomment the line below to print the module docstring (the top docstring)
    #print __doc__
    print "Usage:  %s" % os.path.basename(sys.argv[0])


def main():
    """The main function."""
    args = sys.argv[1:]
    if "-h" in args or "--help" in args:
        usage()
        sys.exit(2)
    # rest of code here
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
