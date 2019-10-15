# 大顶堆特性:
# 首先,這是一個堆,所以是一個完全二叉樹,需要定義樹中節點是按照TreeNode格式
# 之後,大顶堆要求:樹中任意一個節點的值都大于等于其左右子节点的值
# 因为是完全二叉树，使用数据存储更节省空间
# 按照如上特性,还有对应的小顶堆
#
# 堆排序:藉助堆這種數據結構實現的排序算法
# 拆分為建堆和排序兩步操作
# 建堆思路:根據源數組,按照先後順序虛擬構造一個二叉樹,從最後一個非葉子節點所在的數組下標開始往前遍歷數組,
#    每遍歷一個元素,就堆化一次,一直到數組下標為1處時,堆化完成,得到一個大頂堆
# 排序思路:取大頂堆對應數組的下標為1的元素(就是最大的那個),跟數組最後一個元素交換位置,然後對除最後一個元素除外的部分數組堆化
#    然後取新產生的大頂堆的對應數組下標為1的元素,跟數組最後一個元素交換位置,以此類推,最終得到一個從小到大有序的新數組
#
# Python 中內置的有heapq, 是一個小頂堆,直接 import heapq 使用即可.
# 常見用法查看 help(heapq)
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
        
        child_index = value_index * 2
        while child_index < self._count and self._array[child_index // 2] < self._array[child_index]:
            self._array[child_index], self._array[child_index // 2] = self._array[child_index // 2], self._array[child_index]
            child_index = child_index * 2
        

def build_heap(origin_list):
    # 创建堆时要注意在数组存储时是存储在下标为0还是下标为1的位置
    # 下标为1时左右子节点为2*i/2*i+1
    # 下标为0时左右子节点为2*i+1/2*i+2
    length = len(origin_list)-1
    index = length // 2
    while index > 0:
        heapify(origin_list, length, index)
        index -= 1

def heapify(origin_list, length, index):
    while True:
        max_pos = index
        if index*2 <= length and origin_list[index] < origin_list[index*2]:
            max_pos = index*2
        if index*2 + 1 <= length and origin_list[max_pos] < origin_list[index*2 + 1]:
            max_pos = index*2 + 1
        if max_pos == index:
            break
        origin_list[index], origin_list[max_pos] = origin_list[max_pos], origin_list[index]
        index = max_pos

def sort(origin_list):
    build_heap(origin_list)
    last_index = len(origin_list)-1
    while last_index > 1:
        origin_list[1], origin_list[last_index] = origin_list[last_index], origin_list[1]
        last_index -= 1
        heapify(origin_list, last_index, 1)

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
    origin_list = [None, 7, 5, 19, 8, 4, 1, 20, 13, 16]    
    sort(origin_list)
    print(origin_list)