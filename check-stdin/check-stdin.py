#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Check stdin for input.

This checks if stdin contains data (from pipe or redirect). Without this check
it would wait forever for input.  Useful if a script optionally takes a file
via stdin.

Note: this won't work in windows

Tests:
./check-stdin.py  (returns 'not read from stdin')
echo 'test' | ./check-stdin.py  (returns 'test')
./check-stdin.py </proc/loadavg  (returns content from /proc/loadavg)

Ref: http://mail.python.org/pipermail/tutor/2001-February/003472.html

"""

import sys

# isatty() returns true if it's associated with a terminal (meaning no redirect)
if not sys.stdin.isatty():
    # redirected from file or pipe
    stdin_data = sys.stdin.read()
else:
    stdin_data = 'not read from stdin'

print stdin_data
