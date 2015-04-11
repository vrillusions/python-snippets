# vim: set fileencoding=utf-8 :
# -*- coding: utf-8 -*-
"""UTC Formatter needed for FileConfig logger"""
import logging
import time


class UTCFormatter(logging.Formatter):
    converter = time.gmtime
