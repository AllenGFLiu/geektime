# 单链表特性:
# 首先,這是一個链表,需要定義链表中節點是按照Node格式
# 节点中value保存节点值，next指针指向下一个节点
# 链表常见操作包含插入/删除
# 目前实现的是最简单的动作，都是直接插入到最后和删除最后的节点
# 后续还可以增加插入index位置的节点，删除index位置的节点，或者删除特定value的节点
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
        nums.append(tmp_node._value)
        tmp_node = tmp_node._next
    print('->'.join(nums))






if __name__ == '__main__':
    my_list = LinkedList()
    my_list.insert('a')
    my_list.insert('b')
    my_list.insert('c')
    my_list.insert('d')
    my_list.insert('e')
    print(my_list)
    my_list.delete()
    print(my_list)
    reverse_list = my_list.reverse()
    print_node(reverse_list)