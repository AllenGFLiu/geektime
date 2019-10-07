# -*- coding:utf-8 -*-
# 二分查找特性:
# 二分查找作用在一個已經有序的數組上，時間複雜度為O(logn)
# 因為數組存儲數據是需要使用連續內存，如果數據以G為單位，就不適合使用二分查找
# 另外，如果數據量很小，也無需使用二分查找，直接順序存儲即可
#
#
# binsearch 只能作業在不包含重複元素的有序數組上，太局限，所以二分查找有四個變形問題
# 1)binsearch_first_equal 查找第一個值等於給定值的元素 2)binsearch_last_equal 查找最後一個值等於給定值的元素
# 3)binsearch_firste_large_equal 查找第一個大於等於給定值的元素 4)binsearch_last_small_equal 查找最後一個小於等於給定值的元素
#
# Author: AllenGFLiu
# #####################################################


def binsearch(sorted_list, value):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        middle = (low + high) // 2
        if value == sorted_list[middle]:
            return middle
        elif value > sorted_list[middle]:
            low = middle + 1
        else:
            high = middle - 1
    
    return -1


def binsearch_first_equal(sorted_list, value):
    '''查找第一個值等於給定值的元素
    '''
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        midd = low + (high-low) // 2
        midd_value = sorted_list[midd]
        if value > midd_value:
            low = midd + 1
        elif value < midd_value:
            high = midd - 1
        else:
            if midd == 0 or sorted_list[midd-1] != value:
                return midd
            else:
                high = midd - 1
    
    return -1


def binsearch_last_equal(sorted_list, value):
    '''查找最後一個值等於給定值的元素
    '''
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        midd = low + (high-low)//2
        midd_value = sorted_list[midd]
        if value > midd_value:
            low = midd + 1
        elif value < midd_value:
            high = midd - 1
        else:
            if midd == len(sorted_list) - 1 or sorted_list[midd+1] != value:
                return midd
            else:
                low = midd + 1
    
    return -1


def binsearch_firste_large_equal(sorted_list, value):
    '''查找第一個大於等於給定值的元素
    '''
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        midd = low + (high-low) // 2
        midd_value = sorted_list[midd]
        if midd_value >= value:
            if midd == 0 or sorted_list[midd-1] < value:
                return midd
            else:
                high = midd - 1
        else:
            low = midd + 1
    
    return -1


def binsearch_last_small_equal(sorted_list, value):
    '''查找最後一個小於等於給定值的元素
    '''
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        midd = low + (high-low) // 2
        midd_value = sorted_list[midd]
        if midd_value <= value:
            if midd == len(sorted_list)-1 or sorted_list[midd+1] > value:
                return midd
            else:
                low = midd + 1
        else:
            high = midd - 1
    
    return -1


if __name__ == '__main__':
    sorted_list = [0, 1, 4, 6, 9, 10, 10, 34, 55, 69, 110, 110, 110]
    print(binsearch_last_small_equal(sorted_list, 56))

    