#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Example of implementing encryption in python.

Only third party module needed is pycrypto. In ubuntu it's called python-crypto.

Default log level is DEBUG, can alter with LOGLEVEL env variable.

Mostly taken from https://gist.github.com/crmccreary/5610068

TODO: extract iv from ciphertext
TODO: move this file to new template.

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


class MyCrypto(object):
    """Wrapper for encryption functions.

    This goal around this is to create a common api and some convenience
    functions to make things easier. Also if changing to a new service only this
    wrapper needs to be modifed.

    Short list of what this should do:
      - choose between ciphers (AES and Blowfish are the two pycrypto has)
      - have a method to generate a random IV
      - have a method to manage a key that's encrypted by a user's password. an
        example:
          - user enters their password
          - decrypts the actual key (which is just randomness)
          - if encrypting, use the generated IV with the generate key to encrypt
            the content.
          - prepend the IV to encrypted message
      - display as base64 with trailing =s removed (make that optional). Store
        as binary.
      - perhaps move the pkcs7 library to here? that's all it would be needed
        for. Probably not because this is already going to be a large class
      - methods to add and remove IV from message
      - strengthen the provided password using PBKDF2 or scrypt or similar

    """
    def __init__():
        pass


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
    # each separate string you're encoding. Deleting it would likely free up
    # some memory though
    del aes

    text = "tests\n"
    pad_text = encoder.encode(text)
    aes = AES.new(key, AES.MODE_CBC, iv)
    cipher = aes.encrypt(pad_text)
    enc_cipher = base64.b64encode(cipher)
    print("'tests' becomes:", enc_cipher)

    ciphertext = base64.b64decode('hCTVzM84cuWX2LuvKfb8zg==')
    print("ciphertext in hex:", ciphertext.encode('hex'))
    print("Using iv", iv.encode('hex'))
    # iv is first 16 bytes of ciphertext
    #extract_iv = ciphertext[:16]
    #print("Extracted iv", extract_iv.encode('hex'))
    aes = AES.new(key, AES.MODE_CBC, iv)
    text = aes.decrypt(ciphertext)
    print("'hCTVzM84cuWX2LuvKfb8zg==' decrypts to:", encoder.decode(text))
    del aes

    # make sure everything but key is deleted
    del pad_text, iv, cipher, ciphertext, enc_cipher, text
    text = "tests\n"
    pad_text = encoder.encode(text)
    iv = Random.new().read(AES.block_size)
    print("Created iv %s" % iv.encode('hex'))
    aes = AES.new(key, AES.MODE_CBC, iv)
    cipher = aes.encrypt(pad_text)
    # prepend iv to ciphertext
    ciphertext = iv + cipher
    enc_cipher = base64.b64encode(ciphertext)
    print("'tests' becomes:", enc_cipher)

    # make sure everything but key and enc_cipher is deleted
    del aes, pad_text, iv, cipher, ciphertext, text
    print("decrypting", enc_cipher)
    ciphertext = base64.b64decode(enc_cipher)
    print("  in hex:", ciphertext.encode('hex'))
    # extract iv from ciphertext
    iv = ciphertext[:16]
    print("Extracted iv", iv.encode('hex'))
    cipher = ciphertext[16:]
    print("Extracted cipher", cipher.encode('hex'))
    aes = AES.new(key, AES.MODE_CBC, iv)
    text = aes.decrypt(cipher)
    print("Decrypted string:", encoder.decode(text))


    # This version:
    # - encrypt 'tests' with a random iv and a static key
    # - prepend iv to ciphertext
    # - delete iv
    # - extract iv from ciphertext
    # - decrypt using extracted iv and static key
    #
    # Create another version given a password, do sha256 to get a 32 byte key
    # which is then used for encryption
    #
    # Create another version where given password decrypts the actual key that
    # is used for encryption/decryption



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


