#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 13:54:18 2024

@author: sr925041
"""
import math

x = int(input('enter a number x: '))
y = int(input('enter a number y: '))
res = pow(x, y)
print('x**y = '+ str(res))
res1 = int(math.log2(x))
print('log(x) = '+ str(res1))