#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    希尔排序
"""


def shell_sort(data):
    """
    :param data: list<Int>
    :return:
    """
    for step in [4, 2, 1]:
        for i in range(step):
            data[i::step] = simple_insert_sort(data[i::step])


def simple_insert_sort(data):
    """
    :param data: list<Int>
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


if __name__ == "__main__":
    datav = [2, 3, 1, 5, 4, 7, 9]
    print(datav)
    shell_sort(datav)
    print(datav)
