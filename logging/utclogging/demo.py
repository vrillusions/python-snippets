#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""FileConfig logger with utc time

To use a file config for logging and to have utc time output takes a little
extra work. Mainly you have to create a formatter class just to set the
converter attribute to time.gmtime.  See utcformatter.py for that class
"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import sys
import logging
import logging.config


def main(argv=None):
    """The main function.

    :param list argv: List of arguments passed to command line. Default is None,
        which then will translate to having it set to sys.argv.

    :return: Optionally returns a numeric exit code. If not given then will
        default to 0.
    :rtype: int

    """
    logging.config.fileConfig('logging.ini')
    log = logging.getLogger()
    print("see logfile for output")
    log.debug('debug level message')
    log.info('info level message')
    log.warn('warning level message')
    log.error('error level message')
    log.critical('critical level message')


if __name__ == "__main__":
    sys.exit(main())

