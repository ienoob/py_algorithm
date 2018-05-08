#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    插入排序
"""


# normal
def insert_sort(data):
    """
    :param data: list[Int]
    :return:
    """
    if len(data) < 2:
        return data
    for i in range(1, len(data)):
        x = data[i]
        k = i
        for j in range(i-1, -1, -1):
            if data[j] > x:
                data[k] = data[j]
                k -= 1
            else:
                break
        data[k] = x
    return data
