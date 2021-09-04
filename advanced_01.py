# Exercise D1 (30 min)
#
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both
# *args and **kwargs and print them both):
#
# >>> @logged
# ... def func(*args):
# ...
# return 3 + len(args)
# >>> func(4, 4, 4)
# you called func(4, 4, 4)
# it returned 6
# 6


def logged(func):
    def func_wrapper(*args, **kwargs):
        print('You called {.__name__}({}{}{})'.format(func, str(list(args))[1:-1],
                                                      ', ' if kwargs else '',
                                                      ', '.join('{}={}'.format(*pair) for pair in kwargs.items())))
        val = func(*args, **kwargs)
        print('it returned', val)
        return val
    return func_wrapper


# Related logger from: https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string-in-python
import datetime
import logging

# https://stackoverflow.com/questions/32890107/python-standard-logging
# https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
logging.basicConfig(level=logging.DEBUG)
gLog = logging.getLogger(__name__)


class EnterExitLog():
    def __init__(self, funcName):
        self.funcName = funcName

    def __enter__(self):
        gLog.debug('Started: %s' % self.funcName)
        self.init_time = datetime.datetime.now()
        return self

    def __exit__(self, type, value, tb):
        gLog.debug('Finished: %s in: %s seconds' % (self.funcName, datetime.datetime.now() - self.init_time))


def func_timer_decorator(func):
    def func_wrapper(*args, **kwargs):
        with EnterExitLog(func.__name__):
            return func(*args, **kwargs)

    return func_wrapper


# ------------------------------------------------------------------------

@logged
# @func_timer_decorator
def func(*args):
    return 6


def test_run():
    """Running the tests."""
    print(func(4, 4, 4))


if __name__ == '__main__':
    test_run()