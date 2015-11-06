#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks for an IPv4 address and convert to integer."""

from __future__ import division, print_function, unicode_literals
import sys


__version__ = '0.1.0-dev'


def ip2int(ip_address):
    """Takes a dotted IPv4 address and returns an integer."""
    ippart = [int(x) for x in ip_address.split('.')]
    ipint = (ippart[0] << 24) + (ippart[1] << 16) + (ippart[2] << 8) + ippart[3]
    return ipint


def main(argv=None):
    """The main function.

    :param list argv: List of arguments passed to command line. Default is None,
        which then will translate to having it set to sys.argv.

    :return: Optionally returns a numeric exit code. If not given then will
        default to 0.
    :rtype: int

    """
    ip_address = raw_input("Enter an ipv4 address: ")
    print(ip2int(ip_address))


if __name__ == "__main__":
    sys.exit(main())

