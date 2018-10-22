#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    冒泡算法
"""


def bubble_sort(data):
    """
    :param data: list[Int]
    :return:
    """
    if len(data) < 2:
        return data
    d_len = len(data)
    for i in range(d_len-1):
        for j in range(d_len-1-i):
            if data[j] > data[j+1]:
                data[j+1], data[j] = data[j], data[j+1]

    return data
