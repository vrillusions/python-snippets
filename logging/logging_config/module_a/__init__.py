# -*- coding: utf-8 -*-
from __future__ import absolute_import
import logging


# Avoid setting this at file level as the logger will silently be disabled
# unless it's specified in logging.ini or disable_existing_loggers=False when
# calling fileconfig.  As long as you know about those caveats you can set it
# here.  Not knowing this has given me hours of headaches thoug.
#_log = logging.getLogger(__name__)


def hello_world():
    # The purpose of the NullHandler is so if you remove all logging setup from
    # application python won't complain.  Useful if you are making a public
    # module that you don't know how the end user will configure logging.
    # Python 2.7 thing though.
    log = logging.getLogger(__name__).addHandler(logging.NullHandler())
    log.info("Info log message from hello_world() in module_a")
    log.debug("You wont't see this message since logging.ini has this loggers level set to INFO")
    print("Hello world")
