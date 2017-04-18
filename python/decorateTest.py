#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import ctime, sleep

# 声明装饰器
def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()
    return wrappedFunc


@tsfunc
def foo():
    pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()

@staticmethod
def testfunc():
    pass