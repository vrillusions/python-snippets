#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Documentation example.

This is an example of documenting code that will print out nicely when using the
pydoc command.  This is a blend of standard pydoc and epydoc which is used for
the field syntax.  epydoc format is backwards compatible with pydoc, just won't
be displayed as nicely.  Only a small subset of the epydoc fields are given as
an example.

You can view the documentation of this file with `pydoc ./filename.py` (remember
to use the ./ at the beginning)

"""

# can be pulled from version control
__version__ = '1.0'
__author__ = 'John Doe <jdoe@example.com>'


class SomeClase():
    """Some random class.
    
    Takes some various parameters on init, which are documented here because
    (per epydoc): "In C extension modules, extension classes cannot have a 
    docstring attached to the __init__  function"
    
    @param name: Name of someone.
    @param count: Number of people.
    
    """
    def __init__(name=None, count=1):
        self.name = name
        self.count = count
    
    def do_nothing():
        """As the name sugguests, this does nothing."""
        pass
    
    def return_something():
        """Gives something back.
        
        @return: True on success, False on failure
        
        """
        return True
        

def main():
    """The main function."""
    print 'Hello world!'


# Use this so pydoc doesn't execute code
if __name__ == "__main__":
    main()