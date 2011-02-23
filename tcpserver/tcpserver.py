#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""TCP Socket Server.

This creates a socket server that can be accessed using telnet program.

"""

# $Id$
#__version__ = "$Rev$".split(': ')[1].split(' ')[0]
__version__ = ".1"

# standard library imports go here
import sys
import SocketServer
import traceback

#import third party modules here

#import local application/library specific module here


class RequestHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        # The infinite loop allows user to keep issuing commands until quit
        while True:
            line = self.rfile.readline()
            if line.rstrip() == 'help':
                self.wfile.write("You wanted help!\n\n")
                self.wfile.write("say SOMETHING - echo command\n")
                self.wfile.write("quit - close connection\n")
            elif line[:4] == 'say ':
                # echo what they returned
                self.wfile.write(line[4:])
            elif line.rstrip() == 'quit':
                break
            else:
                self.wfile.write("The following command was not recognized:\n")
                self.wfile.write(line)


def main():
	"""The main function."""
    port = 12345
    tcpserver = SocketServer.TCPServer(('127.0.0.1', port), RequestHandler)
    print 'Server started on port', str(port)
    tcpserver.serve_forever()
        

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt, e:
		# Ctrl-c
		raise e
	except SystemExit, e:
		# sys.exit()
		raise e
	except Exception, e:
		print "ERROR, UNEXPECTED EXCEPTION"
		print str(e)
		traceback.print_exc()
		sys.exit(1)
	else:
		# Main function is done, exit cleanly
		sys.exit(0)
