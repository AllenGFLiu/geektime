# 基于Python实现计数排序
# Author: AllenGFLiu
# 计数排序是桶排序的一种特殊情况
# 当要排序的n个数据，所处的范围并不大的时候，比如最大值K，可以把数据划分成K个桶。
#  每个桶内的数据值都是相等的，省掉桶内排序的时间。


def count_sort(nums):
    if len(nums) == 1: return

    max_num = nums[0]
    for num in nums[1:]:
        if num > max_num:
            max_num = num

    c = [0] * (max_num+1)

    for num in nums:
        c[num] += 1

    for i in range(1, max_num+1):
        c[i] += c[i-1]

    r = [0]*len(nums)
    for i in range(len(nums))[::-1]:
        index = c[nums[i]] - 1
        r[index] = nums[i]
        c[nums[i]] -= 1

    for index in range(len(nums)):
        nums[index] = r[index]


if __name__ == '__main__':
    nums = [2,5,3,0,2,3,0,3]
    count_sort(nums)
    print(nums)
