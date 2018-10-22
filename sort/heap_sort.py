#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    堆排序, 选择排序的一种方法
"""


def heap_basic_sort(data):
    """
    :param data: List<Int>
    :return:
    """
    result = []
    build_heap(data)
    while len(data):
        d = data[0]
        result.append(d)
        dl = data.pop()
        if len(data):
            data[0] = dl
        else:
            break
        max_heap(data, 0)
    return result


def build_heap(data):
    d_len = len(data)
    for d in range(d_len//2-1, -1, -1):
        max_heap(data, d)


def max_heap(data, i):
    left = i*2+1
    right = i*2+2
    d_len = len(data)
    lagest = i
    if right < d_len and data[right] > data[lagest]:
        lagest = right
    if left < d_len and data[left] > data[lagest]:
        lagest = left
    if lagest != i:
        data[i], data[lagest] = data[lagest], data[i]
        max_heap(data, lagest)


if __name__ == "__main__":
    dataset = [2, 3, 5, 1, 6]
    heap_basic_sort(dataset)
