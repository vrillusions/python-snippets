# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""ExecutionTime

This class is used for timing execution of code. For example:

    timer = ExecutionTime()
    print 'Hello world!'
    print 'Finished in %s seconds.' % timer.duration()

"""


import time


class ExecutionTime:
    def __init__(self):
        self.start_time = time.time()

    def duration(self):
        return time.time() - self.start_time

