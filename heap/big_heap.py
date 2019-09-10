# 大顶堆特性:
# 首先,這是一個堆,所以是一個完全二叉樹,需要定義樹中節點是按照TreeNode格式
# 之後,大顶堆要求:樹中任意一個節點的值都大于等于其左右子节点的值
# 因为是完全二叉树，使用数据存储更节省空间
# 按照如上特性,还有对应的小顶堆
#
# Author: AllenGFLiu
# #####################################################

class BigHeap():

    def __init__(self, capacity):
        self._array = [0]*(capacity+1)
        self._count = 0
        self._capacity = capacity

    def insert(self, value):
        if self._count == self._capacity:
            return
        self._count += 1
        self._array[self._count] = value
        i = self._count
        while i//2 > 0 and self._array[i] > self._array[i//2]:
            self._array[i], self._array[i//2] = self._array[i//2], self._array[i]
            i = i//2

    def __repr__(self):
        return ' '.join([str(i) for i in self._array])

    def remove(self, value):
        if self._count == 0:
            return 
        if value not in self._array:
            return

        value_index = self._array.index(value)
        self._array[value_index], self._array[self._count] = self._array[self._count], 0
        
        # replace_value = self._array[value_index]
        child_index = value_index * 2
        while child_index < self._count and self._array[child_index // 2] < self._array[child_index]:
            self._array[child_index], self._array[child_index // 2] = self._array[child_index // 2], self._array[child_index]
            child_index = child_index * 2
        


if __name__ == '__main__':
    big_heap = BigHeap(10)
    big_heap.insert(9)
    big_heap.insert(3)
    big_heap.insert(4)
    big_heap.insert(8)
    big_heap.insert(5)
    big_heap.insert(7)
    big_heap.insert(15)
    big_heap.insert(11)
    print(big_heap)
    big_heap.remove(8)
    print(big_heap)