#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Example of implementing encryption in python.

Only third party module needed is pycrypto. In ubuntu it's called python-crypto.

Default log level is DEBUG, can alter with LOGLEVEL env variable.

Mostly taken from https://gist.github.com/crmccreary/5610068

"""

from __future__ import absolute_import, print_function, unicode_literals
import os
import sys
import traceback
import logging
import base64

from Crypto.Cipher import AES
from Crypto import Random

from pkcs7 import PKCS7Encoder


__version__ = 'alpha'


def main():
    """The main function."""
    # TODO: create an AESCipher class or just a general Cipher class or
    # something
    log = logging.getLogger('main')
    # Key length should be 16 (aes128), 24 (aes192), or 32 (aes256) bytes
    # It's doubled here because it's hex, so 64 for aes256
    key = '33f678bcb800d74cc7f718591ac537ef8d99bc23a7a4e7eabec30c680a4f71a5'.decode('hex')
    # Initialization vector is always 16 bytes for aes and we have a convenient
    # variable
    #iv = Random.new().read(AES.block_size)
    iv = '5ecbcf9bc83bd881570a04854a864d69'.decode('hex')
    aes = AES.new(key, AES.MODE_CBC, iv)
    encoder = PKCS7Encoder()
    text = "Example String\n"
    pad_text = encoder.encode(text)
    cipher = aes.encrypt(pad_text)
    enc_cipher = base64.b64encode(cipher)
    print("'Example String' becomes:", enc_cipher)
    # This doesn't have to happen explicitly but you do need to reinit AES for
    # each separate string you're encoding.
    del aes

    text = "tests\n"
    pad_text = encoder.encode(text)
    aes = AES.new(key, AES.MODE_CBC, iv)
    cipher = aes.encrypt(pad_text)
    enc_cipher = base64.b64encode(cipher)
    print("'tests' becomes:", enc_cipher)

    ciphertext = base64.b64decode('hCTVzM84cuWX2LuvKfb8zg==')
    aes = AES.new(key, AES.MODE_CBC, iv)
    text = aes.decrypt(ciphertext)
    print("'hCTVzM84cuWX2LuvKfb8zg==' decrypts to:", encoder.decode(text))



if __name__ == "__main__":
    # DEBUG, INFO, WARNING, ERROR, or CRITICAL
    # This will set log level from the environment variable LOGLEVEL or default
    # to warning. You can also just hardcode the error if this is simple.
    loglevel = getattr(logging, os.getenv('LOGLEVEL', 'DEBUG').upper())
    logformat = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    logging.basicConfig(level=loglevel, format=logformat)
    log = logging.getLogger('ifmain')
    try:
        main()
    except KeyboardInterrupt as e:
        # Ctrl-c
        log.error('Received keyboard interupt')
        raise e
    except SystemExit as e:
        # sys.exit()
        log.debug('Received sys.exit()')
        raise e
    except Exception as e:
        log.error("ERROR, UNEXPECTED EXCEPTION")
        log.error(str(e))
        log.error(traceback.format_exc())
        sys.exit(1)
    else:
        # Main function is done, exit cleanly
        sys.exit(0)


