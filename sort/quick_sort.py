#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    快速排序
"""


def quick_sort(data):
    """
    :param data: list<Int>
    :return:
    """
    if len(data) < 2:
        return data

    d_len = len(data)
    base_action(data, 0, d_len-1)


def base_action(data, start, end):
    if end-start < 1:
        return
    i = start
    j = start+1
    k = end
    while i < k:
        x = data[j]
        if x >= data[i]:
            data[k], data[j] = data[j], data[k]
            k -= 1
        else:
            data[i], data[j] = data[j], data[i]
            i += 1
            j += 1
    base_action(data, start, i-1)
    base_action(data, i+1, end)


if __name__ == "__main__":
    datav = [2, 3, 1, 5, 4, 7, 9]
    print(datav)
    quick_sort(datav)
    print(datav)
