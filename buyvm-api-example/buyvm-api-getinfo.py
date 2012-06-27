#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""BuyVM API Sample.

Basic api example that pulls the information for a certain vm.

"""


import sys
import traceback
import logging
import urllib
import urllib2


__version__ = 'alpha'


def main():
    """The main function."""
    log = logging.getLogger('main()')
    url = "https://manage.buyvm.net/api/client/command.php"
    values = {'key': 'YOUR-API-KEY',
        'hash': 'YOUR-API-HASH',
        'action': 'info',
        'hdd': 'true',
        'mem': 'true',
        'bw': 'true',
        'status': 'true'}
    data = urllib.urlencode(values)
    response = urllib2.urlopen(url, data).read()
    log.debug(response)


if __name__ == "__main__":
    # DEBUG, WARNING, ERROR, or CRITICAL
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('ifmain')
    try:
        main()
    except KeyboardInterrupt, e:
        # Ctrl-c
        log.error('Received keyboard interupt')
        raise e
    except SystemExit, e:
        # sys.exit()
        log.debug('Received sys.exit()')
        raise e
    except Exception, e:
        log.error("ERROR, UNEXPECTED EXCEPTION")
        log.error(str(e))
        log.error(traceback.format_exc())
        sys.exit(1)
    else:
        # Main function is done, exit cleanly
        sys.exit(0)

