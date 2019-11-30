# 队列特性:
# 队列最大的特性就是先进先出，后进后出，最形象的比喻就是排队
# 用数组可以实现队列，链表也可以实现队列
# 队列内声明两个指针：head 和 tail,来表明队列的头部和尾部元素的位置
# 用数组实现的队列还可以支持动态搬移，充分利用存储空间
#
# Author: AllenGFLiu
# #####################################################


# 数组实现队列开始
class ArrayQueue:
    """基于数组的队列，存储的元素个数是固定的。
    head指针指示数组内第一个存储元素的位置
    tail指针指示数组内最后一个存储元素位置的后边一位
    鉴于数组内空间有限，为避免浪费空间，所以在入列时还判断是否有空余位置，若有，有一个搬移动作。
    
    enqueue : 往尾部插入一个value元素
    dequeue : 从头部删除一个元素，并返回值
    """
    def __init__(self, capacity):
        self._array = ['*'] * capacity  # 非必要，只是为了演示数据的跳跃感
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
# 数组实现队列结束


# 链表实现队列开始
class Node:
    
    def __init__(self, value):
        self._value = value
        self.next = None

class ListQueue:
    
    def __init__(self):
        self._tail = None
        self._head = None

    def enqueue(self, value):
        new_node = Node(value)
        if self._tail is None:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        return True

    def dequeue(self):
        if self._head:
            value = self._head._value
            self._head = self._head.next
            return value
            
    def is_empty(self):
        if self._head:
            return False
        return True    
        
    def __repr__(self):
        nums = []
        node = self._head
        while node:
            nums.append(str(node._value))
            node = node.next
        return '<-'.join(nums)        
# 链表实现队列结束




class CircleQueue:
    """循环队列是数组队列的一种特殊情况：
    最开始插入数据后，当tail已经指向最后一格存储空间时，此时继续插入新元素，
    tail指针会指向队列的第一个存储位置(当然，需要先出列一部分数据)。
    当(tail+1)//capacity = head 时，此循环队列已满。
    循环队列不再像普通的数组队列那样需要搬移数据了,
    唯一的缺点就是会浪费tail指针对应的位置空间
    """

    def __init__(self, capacity):
        self._head = 0
        self._tail = 0
        self._capacity = capacity
        self._array = ['*']*capacity

    def enqueue(self, value):
        if (self._tail+1)%self._capacity == self._head:
            return
        self._array[self._tail] = value
        self._tail = (self._tail + 1)%self._capacity

    def dequeue(self):
        if self._head == self._tail:
            return
        tmp = self._array[self._head]
        self._array[self._head] = '*'
        self._head = (self._head + 1)%self._capacity
        return



if __name__ == '__main__':
    # 数组队列测试数据
    # array_queue = ArrayQueue(5)
    # array_queue.enqueue(1)
    # array_queue.enqueue(2)
    # array_queue.enqueue(3)
    # array_queue.enqueue(4)
    # array_queue.enqueue(5)
    # print(array_queue._array)
    # array_queue.dequeue()
    # # print(array_queue._array)
    # array_queue.dequeue()
    # array_queue.dequeue()
    # array_queue.enqueue(6)
    # print(array_queue._array)

    # 链表队列测试数据
    # list_queue = ListQueue()
    # list_queue.enqueue(1)
    # list_queue.enqueue(2)
    # list_queue.enqueue(3)
    # print(list_queue)
    # list_queue.dequeue()
    # list_queue.dequeue()
    # print(list_queue)
    # list_queue.enqueue(4)
    # print(list_queue)

    # 循环队列测试数据
    array_queue = CircleQueue(5)
    array_queue.enqueue(1)
    array_queue.enqueue(2)
    array_queue.enqueue(3)
    array_queue.enqueue(4)
    print(array_queue._array)
    array_queue.dequeue()
    # print(array_queue._array)
    array_queue.dequeue()
    array_queue.dequeue()
    array_queue.enqueue(6)
    print(array_queue._array)
