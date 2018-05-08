#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    归并排序
"""


def merge_sort(data):
    """
    :param data: list[Int]
    :return:
    """
    if len(data) < 2:
        return data
    len_l = 1
    len_d = len(data)
    while len_l > len(data):
        for i in range(len_d//(2*len_l)):
            merge(data, i, len_l)
        len_l *= 2
    return data


def merge(data, start, len_l):
    """
    :param list_a: list[Int]
    :param list_b: list[Int]
    :return:
    """
    x = data[start: start+len_l]
    y = data[start+len_l: start+2*len_l]

    i = 0
    j = 0
    k = 0
    x_len = len(x)
    y_len = len(y)
    while i < x_len and j < y_len:
        if x[i] > y[j]:
            data[k] = y[j]
            j += 1
        else:
            data[k] = x[i]
            i += 1
        k += 1
    if i < x_len:
        for x_ in x[i:]:
            data[k] = x_
            k += 1
    if j < y_len:
        for y_ in y[j:]:
            data[k] = y_
            k += 1


