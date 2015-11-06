"""
src: http://stackoverflow.com/a/23482683
useful to have when testing mail server authentication

doc-testing with example values from RFC 2195

>>> challenge = 'PDE4OTYuNjk3MTcwOTUyQHBvc3RvZmZpY2UucmVzdG9uLm1jaS5uZXQ+'
>>> user = 'tim'
>>> password = 'tanstaaftanstaaf'
>>> target_response = 'dGltIGI5MTNhNjAyYzdlZGE3YTQ5NWI0ZTZlNzMzNGQzODkw'
>>> actual_response = cram_md5(user, password, challenge)
>>> target_response == actual_response
True
"""

import base64
import hashlib
import hmac

def cram_md5(user, password, challenge):
    password = password.encode('utf-8')
    challenge = base64.b64decode(challenge)
    digest = hmac.HMAC(password, challenge, hashlib.md5).hexdigest()
    response = '{} {}'.format(user, digest).encode()
    return base64.b64encode(response).decode()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
