#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
"""Python Template.

This is a template for python.
NOTE: The __future__ imports that make it more v3.x ready were added in v2.6.
Thus this template will only work in python v2.6 or higher.

Note: both a pseudo format of documenting like in this block and rst style
documentation are included.  Choose which one you prefer and be consistent.

Requirements
    Python v2.6 or higher: This is due to the `from future` imports and to make
        this more compatible with version 3.x. For example this template can run
        on both python v2 and v3.

Environment Variables
    LOGLEVEL: overrides the level specified here. Choices are debug, info,
        warning, error, and critical. Default is warning.

"""

# Standard library imports
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import os
import sys
import logging
from optparse import OptionParser

# Third party imports

# Local / custom imports (stuff that's usually another file in directory)


# Follow http://semver.org/ versioning conventions
__version__ = '0.1.0-dev'


# Logger config
# DEBUG, INFO, WARNING, ERROR, or CRITICAL
# This will set log level from the environment variable LOGLEVEL or default
# to warning. You can also just hardcode the error if this is simple.
_LOGLEVEL = getattr(logging, os.getenv('LOGLEVEL', 'WARNING').upper())
_LOGFORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=_LOGLEVEL, format=_LOGFORMAT)


# Examples on documenting functions and classes. You can also look in to making
# documentation that can be generated by sphinx. See http://sphinx-doc.org
#
# A lot of this came from
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
def sample_def(meh=None):
    """This is a sample function.

    Long description would go here.

    Args:
        meh: I guess this would have something here

    Returns:
        The word 'hello'

    """
    log = logging.getLogger(__name__)
    if meh:
        log.debug('meh was set to {}'.format(meh))
    log.info('Returning hello')
    return 'hello'


class SampleClass(object):
    """This is a sample class.

    Just illustrating how a docblock would look. Note how this class inherits
    from `object`. In Python v2 this declares this as a 'new style' class. In
    Python v3 this is the default and no longer need the `object` (but it will
    still work if included.

    Attributes:
        blah: This stores some number of blahs

    """
    def __init__(self):
        """Inits SampleClass."""
        self._log = logging.getLogger(__name__)
        self.blah = 3

    def get_blah(self):
        """Returns the value of blah."""
        self._log.debug('Returning blah')
        return self.blah

    def set_blah(self, value):
        """Sets the value of blah."""
        self._log.debug('Setting blah')
        self.blah = value


def _parse_opts(argv=None):
    """Parse the command line options.

    :param list argv: List of arguments to process. If not provided then will
        use optparse default
    :return: options,args where options is the list of specified options that
        were parsed and args is whatever arguments are left after parsing all
        options.

    """
    parser = OptionParser(version='%prog {}'.format(__version__))
    parser.set_defaults(verbose=False)
    parser.add_option('-c', '--config', dest='config', metavar='FILE',
        help='Use config FILE (default: %default)', default='config.ini')
    parser.add_option('-v', '--verbose', dest='verbose', action='store_true',
        help='Be more verbose (default is no)')
    (options, args) = parser.parse_args(argv)
    return options, args


def main(argv=None):
    """The main function.

    :param list argv: List of arguments passed to command line. Default is None,
        which then will translate to having it set to sys.argv. Typically is
        used in conjuction with option and contains the information added to the
        end after all the options.

    :return: Optionally returns a numeric exit code. If not 0 then assume an
        error has happened.
    :rtype: int

    """
    log = logging.getLogger()
    if argv is None:
        argv = sys.argv
    #(options, args) = _parse_opts(argv)
    # If not using args then don't bother storing it
    options = _parse_opts(argv)[0]
    if options.verbose:
        log.setLevel(logging.DEBUG)
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
    sys.exit(main())

