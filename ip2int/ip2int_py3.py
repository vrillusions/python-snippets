#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asks for an IPv4 address and convert to integer.

In Python v3.3 the ipaddress module was added so this is much simpler
"""
import sys
import ipaddress


__version__ = '0.1.0-dev'


def main(argv=None):
    """The main function.

    :param list argv: List of arguments passed to command line. Default is None,
        which then will translate to having it set to sys.argv.

    :return: Optionally returns a numeric exit code. If not given then will
        default to 0.
    :rtype: int

    """
    if argv is None:
        argv = sys.argv
    if argv[1]:
        ip_address = argv[1]
    else:
        ip_address = input("Enter an ipv4 dotted quad or decimal: ")
    if ip_address.isdigit():
        # Received a decimal, convert to ip
        print(str(ipaddress.ip_address(int(ip_address))))
    else:
        print(int(ipaddress.ip_address(ip_address)))


if __name__ == "__main__":
    sys.exit(main())

