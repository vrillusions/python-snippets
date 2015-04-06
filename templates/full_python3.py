#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python Template.

This is a template for python 3.  It's only been verified on python v3.3

Environment Variables
    LOGLEVEL: overrides the level specified here. Choices are debug, info,
        warning, error, and critical. Default is warning.

"""

# Standard library imports
import os
import sys
import logging
import argparse

# Third party imports

# Local / custom imports (stuff that's usually another file in directory)


# Follow http://semver.org/ versioning conventions
__version__ = '0.1.0-dev'


def sample_def(meh=None):
    """This is a sample function.

    Long description would go here.

    :param string meh: This would describe the meh parameter

    :return: The word hello
    :rtype: string

    """
    log = logging.getLogger(__name__)
    if meh:
        log.debug('meh was set to {}'.format(meh))
    log.info('Returning hello')
    return 'hello'


class SampleClass():
    """This is a sample class.

    Just illustrating how a docblock would look.

    """
    _log = logging.getLogger(__name__)

    def __init__(self):
        """Inits SampleClass."""
        self.blah = 3

    def get_blah(self):
        """Returns the value of blah."""
        self._log.debug('Returning blah')
        return self.blah

    def set_blah(self, value):
        """Sets the value of blah."""
        self._log.debug('Setting blah')
        self.blah = value


def main(args=None):
    """The main function.

    :param obj args: arguments as processed from argparse.

    :return: Optionally returns a numeric exit code. If not 0 then assume an
        error has happened.
    :rtype: int

    """
    log = logging.getLogger()
    log.debug('Printing hello world to screen')
    print("hello world!")
    print(sample_def())
    samplecls = SampleClass()
    print(samplecls.get_blah())
    log.debug('Changing log level to error')
    log.setLevel(logging.ERROR)
    log.error('The next log message will not be visible')
    log.debug('Should not see this')
    log.setLevel('DEBUG')
    log.info('Log level set back to DEBUG')


if __name__ == "__main__":
    # Marking everything as "private" (prefix with underscore) as these
    # variables are considered globals since they're not within a function.
    #
    # Configure logging only if called directly
    _loglevel = getattr(logging, os.getenv('LOGLEVEL', 'WARNING').upper())
    _logformat = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=_loglevel, format=_logformat)
    _log = logging.getLogger()

    # Same for argument parsing
    _parser = argparse.ArgumentParser(description='Example description')
    _parser.add_argument(
        '--version', action='version',
        version='%(prog)s {}'.format(__version__))
    _parser.add_argument(
        '-v', '--verbose', dest='verbose', action='count',
        help='increase verbosity (up to 2 times)')
    _parser.add_argument(
        '-c', '--config', dest='config', metavar='FILE',
        help='Use config FILE (default: %(default)s)', default='config.ini')
    args = _parser.parse_args()

    if args.verbose:
        if args.verbose == 1:
            _log.setLevel(logging.INFO)
            _log.info('Log level set to INFO')
        if args.verbose >= 2:
            _log.setLevel(logging.DEBUG)
            _log.info('Log level set to DEBUG')

    sys.exit(main(args))
