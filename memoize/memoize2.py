# vim: set fileencoding=utf-8 :
"""Another way to do memoize

Like this one over other because it's shorter. Also I think this one does more
than first version. I guess the downside is it's a nested function instead of a
class. Not sure what issues may arise from that.

source: https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
"""

import functools
import timeit
import time


def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer


# Rest of this is just used for testing

class ExecutionTime(object):
    def __init__(self):
        self.start_time = time.time()

    def duration(self):
        return time.time() - self.start_time


@memoize
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n):
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)


@memoize
def sleepy(sleep_length):
    print("yawn...")
    time.sleep(sleep_length)
    return("OK I'm awake")

def sleepy2(sleep_length):
    print("yawn...")
    time.sleep(sleep_length)
    return("OK I'm awake")


if __name__ == "__main__":
    # The higher the number doesn't change the time that much.  Also any higher
    # than 300 or so will hit a recursion limit. The recommended approach would
    # be to use a dictionary to cache the values but we're not testing that.
    # Main reason for the longer time is when not memoized it takes the same
    # amount of time for second call
    setup = 'from __main__ import memoize, fibonacci, fibonacci2'
    fibnum = 100
    print("memoized version of fibonacci({})".format(fibnum))
    print(timeit.timeit("fibonacci({0}); fibonacci({0})".format(fibnum), setup=setup))
    print("non-memoized version of fibonacci({})".format(fibnum))
    print(timeit.timeit("fibonacci2({0}); fibonacci2({0})".format(fibnum), setup=setup))

    # Using "sleepy" may be a better test as memoize is commonly used where
    # a single call to the function takes a long time, not recursion
    #
    # This also highlights an important difference. memoize caches the result of
    # the function so the "yawn" print statement doesn't get cached and so the
    # memoized version won't output it the subsequent times it's run
    sleep_length = 10
    print("memoized version of sleepy({}), called twice".format(sleep_length))
    timer = ExecutionTime()
    print(sleepy(sleep_length))
    print(sleepy(sleep_length))
    print("Duration: {}".format(timer.duration()))
    print("non-memoized version of sleepy({}), called twice".format(sleep_length))
    timer = ExecutionTime()
    print(sleepy2(sleep_length))
    print(sleepy2(sleep_length))
    print("Duration: {}".format(timer.duration()))
