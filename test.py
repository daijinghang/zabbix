#!/usr/bin/env python
# -*- coding:utf-8 -*-
def funA(fun):
    print (fun())

def funB():
    print ('B')
    return 2


funA(funB)