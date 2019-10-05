# 循環队列特性:
# 队列最大的特性就是先进先出，后进后出，最形象的比喻就是排队
# 使用數組實現的非循環順序隊列，會存在數據搬移的問題，均攤時間複雜度為O(1)
# 使用循環順序隊列可以避免數據搬移，因為是一個環
#
# Author: AllenGFLiu
# #####################################################


class CircleQueue():
    """基于数组的队列，存储的元素个数是固定的。
    head指针指示数组内第一个存储元素的位置
    tail指针指示数组内最后一个存储元素位置的后边一位
    循環隊列的隊空判定條件是head == tail, 隊滿的判定條件是(tail+1)%n == head

    enqueue : 往尾部插入一个value元素
    dequeue : 从头部删除一个元素，并返回值
    """

    def __init__(self, capacity):
        self._array = ['*']*capacity
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, value):
        if (self._tail + 1)% self._capacity == self._head:
            return
        self._array[self._tail] = value
        self._tail = (self._tail+1) % self._capacity

    def dequeue(self):
        if self._head == self._tail:
            return
        return_value = self._array[self._head]
        self._array[self._head] = '*'
        self._head = (self._head+1) % self._capacity
        return return_value

    def __repr__(self):
        return ''.join(self._array)


if __name__ == '__main__':
    cq = CircleQueue(5)
    cq.enqueue('a')
    cq.enqueue('b')
    cq.enqueue('c')
    cq.enqueue('d')
    print(cq)
    cq.dequeue()
    cq.enqueue('e')
    print(cq)
