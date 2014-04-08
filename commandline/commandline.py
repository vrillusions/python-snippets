#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
"""Example of an interactive command line script.

ref:
    http://pymotw.com/2/cmd/index.html
    https://docs.python.org/2/library/cmd.html

"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import sys
import cmd


class MyApp(cmd.Cmd):
    intro = "Type 'help' for a list of commands"
    #prompt = 'cmd> '

    def emptyline(self):
        """Called when user hits enter again without typing anything.

        Default is to repeat last cmd. Instead do nothing

        """
        pass

    def do_hello(self, line):
        """Hello..."""
        print("world")

    def do_EOF(self, line):
        """Type ctrl-d or 'quit' to exit."""
        # Add print to insert line break at end
        print()
        return True

    def do_quit(self, line):
        """Quit"""
        return True


if __name__ == "__main__":
    MyApp().cmdloop()

