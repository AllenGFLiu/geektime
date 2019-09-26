# 栈特性:
# 队列最大的特性就是先进后出，后进先出，最形象的比喻就是摞在一起的盘子
# 用数组可以实现栈，链表也可以实现栈
# 栈主要有两个动作：压栈push和出栈pop
#
# Author: AllenGFLiu
# #####################################################
import sys
sys.path[0]='D:\\GitHub\\geektime'

from linked_list.one_way_linked_list import LinkedList


class ListStack():
    """使用之前实现的单链表实现栈的数据结构。
    基于链表的栈，没有容量限制。
    
    push:压入栈，压入成功则返回True.

    pop:出栈，正常出栈返回出栈的值，若无数据可出，则返回None.
    """
    def __init__(self):
        self.list = LinkedList()

    def push(self, value):
        self.list.insert(value)
        return True

    def pop(self):
        self.list.delete()

    def __repr__(self):
        return self.list


if __name__ == '__main':
    my_stack = ListStack()
    my_stack.push('a')
    my_stack.push('b')
    my_stack.push('c')
    print(my_stack)
