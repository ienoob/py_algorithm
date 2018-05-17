#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    寻找最大子数组
"""

# 思路1 暴力求解
def direct_max_subarray(data):
    """
    :param data: list[Int]
    :return: max value
    """
    d_len = len(data)
    d_max = -1*2<<31
    d_i = -1
    d_j = -1
    for i in range(d_len):
        s = 0
        for j in range(i, d_len):
            s += data[j]
            if s > d_max:
                d_max = s
                d_i = i
                d_j = j
    print("start and end index is {}, {}".format(d_i, d_j))
    return d_max, d_i, d_j

#  思路2 分治方法
# 分为三种情况进行处理
def max_subarray_dis(start, end, data):
    if start == end:
        return data[start], start, end
    if start > end:
        return -1 * 2 << 31, -1, -1
    mid = (start+end)//2
    left_max, left_s, left_e = max_subarray_dis(start, mid-1, data)
    right_max, right_s, right_e = max_subarray_dis(mid+1, end, data)

    mid_max, mid_s, mid_t = max_sub_cross(start, mid, end, data)

    if left_max >= mid_max and left_max >= mid_max:
        return left_max, left_s, left_e
    if right_max >= mid_max and right_max >= left_max:
        return right_max, right_s, right_e
    return mid_max, mid_s, mid_t



def max_sub_cross(start, mid, end, data):
    left_i = mid
    left_m = -1 * 2 << 31
    s = 0
    for i in range(mid, start-1, -1):
        s += data[i]
        if s > left_m:
            left_m = s
            left_i = i

    right_i = mid
    right_m = -1 * 2 << 31
    s = 0
    for i in range(mid, end+1):
        s += data[i]
        if s > right_m:
            right_m = s
            right_i = i
    return left_m + right_m - data[mid], left_i, right_i


