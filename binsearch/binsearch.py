# -*- coding:utf-8 -*-
# 二分查找特性:
# 二分查找作用在一個已經有序的數組上，時間複雜度為O(logn)
# 因為數組存儲數據是需要使用連續內存，如果數據以G為單位，就不適合使用二分查找
# 另外，如果數據量很小，也無需使用二分查找，直接順序存儲即可
#
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


if __name__ == '__main__':
    sorted_list = [0, 1, 4, 6, 9, 10, 22, 34, 55, 69, 99, 110, 138, 1111]
    print(binsearch(sorted_list, 1338))

    