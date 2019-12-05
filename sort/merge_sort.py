# 基于Python实现归并排序
# Author: AllenGFLiu
# 归并排序使用分治思想，对原始数组进行递归拆分，待拆分到单独的元素时进行合并
# 合并方法使用双指针方法，动态指定较小元素插入到临时list中，最后做个整体的覆盖替换
# 归并排序时间复杂度为O(nlogn), 空间复杂度为O(n)


def merge_sort(nums):

    def merge(array, p, q, r):  # 与合并两个有序链表类似的方法
        tmp_list = []
        i = p
        j = q+1
        while i<=q and j<=r:
            if array[i] < array[j]:
                tmp_list.append(array[i])
                i += 1
            else:
                tmp_list.append(array[j])
                j += 1

        if i<=q:  # 最开始定义i=p;p到q是一个分割区间；i<=q说明还有元素没有插入tmp_list中
            tmp_list.extend(array[i:q+1])
        if j<=r:  # 同上
            tmp_list.extend(array[j:r+1])

        array[p:r+1] = tmp_list  # 整体覆盖替换原数组[p:r+1]区间内的元素

    def recursive_divide(array, p, r):
        if p>=r: return

        q = (p+r)//2
        recursive_divide(array, p, q)
        recursive_divide(array, q+1, r)
        merge(array, p, q, r)

    recursive_divide(nums, 0, len(nums)-1)

if __name__ == '__main__':
    nums = [11, 8, 3, 9, 7, 1, 2, 5]
    merge_sort(nums)
    print(nums)
