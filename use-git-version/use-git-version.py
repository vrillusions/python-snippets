#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Using git describe for version number

Runs git describe and will attempt to use that for version

"""

from subprocess import Popen, PIPE


git_version = Popen(['git', 'describe', '--always'], 
    stdout=PIPE, stderr=PIPE).stdout.read().strip()
__version__ = git_version if git_version else ''


def main():
    """The main function."""
    print 'Version:', __version__


if __name__ == "__main__":
    main()

