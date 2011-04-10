#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Logging template.

This is an example of using the logging function.

As an aside, calling this file "logging.py" messed up import

"""

import sys
import os
import traceback
import logging

class SomeClass:
    def __init__(self):
        self._log = logging.getLogger('%s.%s' % (__name__, self.__class__.__name__))
    
    def error(self):
        self._log.error('test error message')

def main():
    """The main function."""
    # Log Levels in descending order
    # debug
    # warning
    # error
    # critical
    logging.basicConfig(level=logging.WARNING)
    log = logging.getLogger(__name__)
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