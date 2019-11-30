#-*- coding:utf-8 -*-
# 栈特性:
# 队列最大的特性就是先进后出，后进先出，最形象的比喻就是摞在一起的盘子
# 用数组可以实现栈，链表也可以实现栈
# 栈主要有两个动作：压栈push和出栈pop
#
# Author: AllenGFLiu
# #####################################################


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class ListStack:
    """基於單鏈錶實現棧的數據結構。
    基于链表的栈，没有容量限制。
    
    push:入栈.

    pop:出栈，正常出栈返回出栈的值，若无数据可出，则返回None.
    """
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node 

    def pop(self):
        if self.head:
            value = self.head.val
            self.head = self.head.next

    def __repr__(self):
        nums = []
        node = self.head
        while node:
            nums.append(node.val)
            node = node.next
        return '->'.join(nums)


if __name__ == '__main__':
    my_stack = ListStack()
    my_stack.push('a')
    my_stack.push('b')
    my_stack.push('c')
    print(my_stack)
    my_stack.pop()
    print(my_stack)
