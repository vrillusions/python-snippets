# -*- coding: utf-8 -*-
from __future__ import absolute_import
import logging


# Don't place this here or else it will complain unless you have
# disable_existing_loggers=False set when calling fileconfig
#_log = logging.getLogger(__name__)


def hello_world():
    log = logging.getLogger(__name__)
    log.info("Info log message from hello_world() in module_b.hello_world")
    log.debug("this debug message you will see since it uses the root loggers setting of debug")
    print("Hello world")
