# coding=UTF-8
from time import time

times = {}


def countTime(func):
    def wrapper(*args, **kw):
        funcName = func.__name__
        fst = time()
        res = func(*args, **kw)
        fet = time()
        if times.get(funcName) is None:
            times[funcName] = 1
        else:
            times[funcName] += 1
        print('func {} run {} times,this time used {}s'.format(funcName, times[funcName], fet - fst))
        return res

    return wrapper


