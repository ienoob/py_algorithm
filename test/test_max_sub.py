#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    测试最大子数组
"""
import time
import random
from find_max_subarray import direct_max_subarray, max_subarray_dis

length = 10000
array = [random.randint(-length, length) for i in range(length)]
print(length)

start = time.clock()
print(direct_max_subarray(array))
print("cost {}s".format(time.clock()-start))

start = time.clock()
print(max_subarray_dis(0, length-1, array))
print("cost {}s".format(time.clock()-start))