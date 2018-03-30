#  encoding : utf8

import datetime
import time
import collections

counter = collections.Counter()


def fib1(n):
    # easiest way to implement fibnocci numbers
    assert (isinstance(n, int) and (n > 0)
            ), ' n should be an positive interger'
    if n == 0:
        return 0
    if n < 2:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    # count how many time we iterate fib2 function
    if n == 0:
        return 0
    if n < 2:
        return n
    else:
        counter[n - 1] += 1
        counter[n - 2] += 2
        return fib2(n - 1) + fib2(n - 2)

################
# yield (series)
################


def fib3(n):

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def memoize(f):
    cache = {}

    def decorated_function(args):
        if args not in cache:
            cache[args] = f(args)
        return cache[args]
    return decorated_function

#############################
# create a memorize decorator
#############################


@memoize
def fib(n):
    if n == 0:
        return 0
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

###############
# general form
###############


def mydecorator(function):
    def _mydecorator(*args, **kw):
        # Do stuff here before calling the original function
        # call the function
        res = function(*args, **kw)
        # Do more stuff after calling the function
        return res

    # return the sub-function
    return _mydecorator


if __name__ == '__main__':
    ###################
    # 1. recursive fib
    ###################
    t1 = time.time()
    n = 30
    ans1 = fib1(n)
    t2 = time.time()
    print('fib({})={},\ttime:{:.2f} s'.format(n, ans1, t2 - t1))
    # ##################
    # # 2. counter
    # ##################
    t1 = time.time()
    n = 30
    counter = collections.Counter()
    ans2 = fib2(n)
    t2 = time.time()
    print('n={}, most counter:{},\n\ttime:{:.2f}s'.format(
        n, counter.most_common()[0], t2 - t1))
    # #################
    # # 3. yield
    # #################
    t1 = time.time()
    n = 30
    ans3 = list(fib3(n))
    t2 = time.time()
    print('yield fib({}),\n\t series:{},\n\ttime:{:.2f}'.format(
        n, ans3, t2 - t1
    ))
    #################
    # 4. decorated fib
    #################
    t1 = time.time()
    n = 30
    ans4 = fib(n)
    t2 = time.time()
    print('cached fib({}) = {}, \n\ttime:{:.2f}'.format(
        n, ans4, t2 - t1
    ))
