# 基于Python实现快速排序
# Author: AllenGFLiu
# 快速排序简称快排，随机取原始数组的最后一位作为pivot，循环原数组取元素与pivot对比
# 比pivot小的放一块， 比pivot大的放一块
# 递归再划分以上两块集合
# 快排中的划分方法使用直接交换数组元素来进行原地排序
# 时间复杂度为O(nlogn), 空间复杂度为O(1)
# 正因为空间复杂度比归并排序低，所以快排相比归并应用的更广泛


def quick_sort(nums):

    def partition(array, p, r):
        pivot = array[r]
        i = p
        for j in range(p, r+1):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]
                i += 1
        array[i], array[r] = array[r], array[i]

        return i

    def recursive_divide(array, p, r):
        if p >= r: return

        q = partition(array, p, r) # 返回pivot所在的索引，并把原始数组分成三份：比pivot小的/pivot/比pivot大的
        recursive_divide(array, p, q-1) # 让比pivot小的部分递归
        recursive_divide(array, q+1, r) # 让比pivot大的部分递归

    recursive_divide(nums, 0, len(nums)-1)


if __name__ == '__main__':
    nums = [6, 11, 3, 9, 8]
    quick_sort(nums)
    print(nums)
        

