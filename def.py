#!/usr/bin/env python
# -*- encoding: utf-8 -*-

def pow_example(n, p=2):
    '''works only with p >= 1'''
    if p <= 1:
        return n
    return n * pow_example(n, p-1)

print (pow_example(3, 3))

print('test')
