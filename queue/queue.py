# 队列特性:
# 队列最大的特性就是先进先出，后进后出，最形象的比喻就是排队
# 用数组可以实现队列，链表也可以实现队列
# 队列内声明两个指针：head 和 tail,来表明队列的头部和尾部元素的位置
# 用数组实现的队列还可以支持动态搬移，充分利用存储空间
#
# Author: AllenGFLiu
# #####################################################


class ArrayQueue:
    """基于数组的队列，存储的元素个数是固定的。
    head指针指示数组内第一个存储元素的位置
    tail指针指示数组内最后一个存储元素位置的后边一位
    鉴于数组内空间有限，为避免浪费空间，所以在入列时还判断是否有空余位置，若有，有一个搬移动作。
    
    enqueue : 往尾部插入一个value元素
    dequeue : 从头部删除一个元素，并返回值
    """
    def __init__(self, capacity):
        self._array = ['*'] * capacity
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, value):
        if self._tail == self._capacity:
            if self._head == 0:
                return
            for i in range(self._head, self._capacity):
                self._array[i-self._head] = self._array[i]
                self._array[i] = '*'
            self._tail -= self._head
            self._head = 0

        
        self._array[self._tail] = value
        self._tail += 1

    def dequeue(self):
        if self._head == self._tail:
            return
        tmp = self._array[self._head]
        self._array[self._head] = '*'
        self._head += 1
        return tmp




class ListQueue:
    pass


class CircleQueue:
    pass


if __name__ == '__main__':
    array_queue = ArrayQueue(5)
    array_queue.enqueue(1)
    array_queue.enqueue(2)
    array_queue.enqueue(3)
    array_queue.enqueue(4)
    array_queue.enqueue(5)
    print(array_queue._array)
    array_queue.dequeue()
    # print(array_queue._array)
    array_queue.dequeue()
    array_queue.dequeue()
    array_queue.enqueue(6)
    print(array_queue._array)
