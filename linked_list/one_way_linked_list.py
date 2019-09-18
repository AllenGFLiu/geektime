# -*- coding:utf-8 -*-
# 单链表特性:
# 首先,這是一個链表,需要定義链表中節點是按照Node格式
# 节点中value保存节点值，next指针指向下一个节点
# 链表常见操作包含插入/删除
# 目前实现的是最简单的动作，都是直接插入到最后和删除最后的节点
# 后续还可以增加插入index位置的节点，删除index位置的节点，或者删除特定value的节点
#
# reverse:實現鏈錶反轉
#
# Author: AllenGFLiu
# #####################################################


class Node:
    def __init__(self, value):
        self._value = value
        self._next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail._next = new_node
        self.tail = new_node

    def __repr__(self):
        if self.head == None:
            return 'None'
        nums = []
        node = self.head
        while node:
            nums.append(node._value)
            node = node._next
        return '->'.join(nums)

    def delete(self):
        if self.head == None:
            return
        node = self.head
        last_node = None
        while node != self.tail:
            last_node = node
            node = node._next
        last_node._next = None
        self.tail = last_node

    def reverse(self):
        """反轉鏈錶.
        此方法目前是定義在類中,常規用法是獨立在外部聲明和使用.
        在外部使用時,傳入一個頭結點就可以按照節點的next,順藤摸瓜得到并反轉整個鏈錶.
        """
        node = self.head
        reverse_node = None
        while node:
            next_node = node._next
            node._next = reverse_node
            reverse_node = node
            node = next_node
        return reverse_node


def print_node(node):
    tmp_node = node
    nums = []
    while tmp_node:
        nums.append(str(tmp_node._value))
        tmp_node = tmp_node._next
    print('->'.join(nums))


def merge_two_sorted_list(l1, l2):
    """合併兩個有序鏈錶,返回新的有序鏈錶.
    取兩個鏈錶的第一個值,比對大小,取最小值插入到新鏈錶,
    然後較小值所在的鏈錶節點後移一位,再次比對節點值大小,以此類推,直到某一個鏈錶全部比對完畢.
    最後,新鏈錶next指針指向比對完畢還有剩餘的鏈錶,就產生了把兩個鏈錶合在一起的新的有序鏈錶.
    """
    
    if l1 and l2:  # 如果兩個原始鏈錶有一個為空或者都為空,就直接返回 l1 or l2 即可.
        p1, p2 = l1, l2
        head = Node(None)
        tail = head
        while p1 and p2:
            if p1._value <= p2._value:
                tail._next = p1
                p1 = p1._next
            else:
                tail._next = p2
                p2 = p2._next
            tail = tail._next
        tail._next = p1 if p1 else p2
        return head._next
    return l1 or l2


if __name__ == '__main__':
    # my_list = LinkedList()
    # my_list.insert('a')
    # my_list.insert('b')
    # my_list.insert('c')
    # my_list.insert('d')
    # my_list.insert('e')
    # print(my_list)
    # my_list.delete()
    # print(my_list)
    # reverse_list = my_list.reverse()
    # print_node(reverse_list)
    l1 = LinkedList()
    l1.insert(3)
    l1.insert(4)
    l1.insert(9)
    l2 = LinkedList()
    l2.insert(2)
    l2.insert(5)
    l2.insert(6)
    new_list = merge_two_sorted_list(l1.head, l2.head)
    print_node(new_list)