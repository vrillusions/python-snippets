#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using a logging config plus logging modules."""
from __future__ import absolute_import
import os
import sys
import logging
import logging.config

import module_a
import module_b


def hello_world():
    log = logging.getLogger(__name__)
    log.info("Info log in hello_world() in main file")
    print("hello world!")


if __name__ == '__main__':
    # This is your standard way of using LOGLEVEL environment variable to
    # control what's output to console. Think of this also how you'd handle a
    # --verbose or --debug option. It is only used for the console log, file log
    # level is handled in the logging.ini file
    _loglevel = getattr(logging, os.getenv('LOGLEVEL', 'INFO').upper())
    _logformat = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # The disable_existing_loggers can be really important depending on where
    # you call getLogger in modules.  You should setup your module so it doesn't
    # need it but this option will save you a lot of headaches.
    logging.config.fileConfig('logging.ini', disable_existing_loggers=False)

    # This is where we setup the level of output to screen
    _console_handler = logging.StreamHandler()
    _console_handler.setFormatter(logging.Formatter(_logformat))
    _console_handler.setLevel(_loglevel)

    # This attaches the above handler to the root logger and thus all logs
    _log = logging.getLogger()
    _log.addHandler(_console_handler)

    module_a.hello_world()
    module_b.hello_world()
    hello_world()
    print("done")
