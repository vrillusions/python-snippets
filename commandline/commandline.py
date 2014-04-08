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

    def get_names(self):
        """Filter out commands not to show in help.

        Note: while 'help' doesn't show you can still do a 'help EOF' and it
        will show the docstring for do_EOF().

        """
        ignored = ('do_EOF', 'do_admin')
        names = [x for x in dir(self.__class__) if x not in ignored]
        return names

    def emptyline(self):
        """Called when user hits enter again without typing anything.

        Default is to repeat last cmd. Instead do nothing

        """
        pass

    def do_admin(self, line):
        """Super secret command."""
        # this is filtered, see get_names()
        print('My password is: correct horse battery staple')

    def do_EOF(self, line):
        """Type ctrl-d or 'quit' to exit."""
        # Add print to insert line break at end
        print()
        return True

    def do_hello(self, line):
        """Hello..."""
        print("world")

    def do_quit(self, line):
        """Quit"""
        return True


if __name__ == "__main__":
    MyApp().cmdloop()

