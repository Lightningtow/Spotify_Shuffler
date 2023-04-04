# import sys
# import threading
#
# from urllib3.connectionpool import xrange
#
# from data import AUTH
#
# try:
#     import thread
# except ImportError:
#     import _thread as thread
#
# try:  # use code that works the same in Python 2 and 3
#     range, _print = xrange, print
#
#
#     def print(*args, **kwargs):
#         flush = kwargs.pop('flush', False)
#         _print(*args, **kwargs)
#         if flush:
#             kwargs.get('file', sys.stdout).flush()
# except NameError:
#     pass
#
#
# def cdquit(fn_name):
#     # print to stderr, unbuffered in Python 2.
#     print('{0} took too long'.format(fn_name), file=sys.stderr)
#     sys.stderr.flush()  # Python 3 stderr is likely buffered.
#     thread.interrupt_main()  # raises KeyboardInterrupt
#
#
# def exit_after(s):
#     '''
#     use as decorator to exit process if
#     function takes longer than s seconds
#     '''
#
#     def outer(fn):
#         def inner(*args, **kwargs):
#             timer = threading.Timer(s, cdquit, args=[fn.__name__])
#             timer.start()
#             try:
#                 result = fn(*args, **kwargs)
#             finally:
#                 timer.cancel()
#             return result
#
#         return inner
#
#     return outer
#
#
# @exit_after(5)
# def infin():
#     sp = AUTH
#     user = sp.me()