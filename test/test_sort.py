#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import time
import copy
from sort.insert_sort import insert_sort
from sort.merge_sort import merge_sort
from sort.bubble_sort import bubble_sort
from sort.heap_sort import heap_basic_sort

# 随机数组
length = 10000
array = [random.randint(0, length-1) for i in range(length)]

start = time.clock()
insert_sort(copy.deepcopy(array))
print("insert sort cost {}s".format(time.clock()-start))

start = time.clock()
merge_sort(copy.deepcopy(array))
print("merge sort cost {}s".format(time.clock()-start))

start = time.clock()
bubble_sort(copy.deepcopy(array))
print("bubble sort cost {}s".format(time.clock()-start))

start = time.clock()
heap_basic_sort(copy.deepcopy(array))
print("heap sort cost {}s".format(time.clock()-start))

start = time.clock()
array.sort()
print("python self sort cost {}s".format(time.clock()-start))
