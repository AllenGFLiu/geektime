# -*- coding:utf-8 -*-
# 在单链表之上增加多层索引的数据结构就是跳表
# 跳表是动态数据结构，查找/插入/删除的时间复杂度都是O(logn), 空间复杂度是O(n),是以空间换时间的设计理念
# 跳表的节点在插入时通过random的形式确定插入跳表后拥有的层数，具体看insert方法的注释
# 跳表示例图：
# | |-------->| |-------->
# | |-------->| |-------->
# | |-------->| |-------->
# | |-------->|6|-------->
# | |-->| |-->| |-------->
# | |-->|3|-->| |-->|7|-->之后的省略
# 其中第一个节点是self._head节点，定义为一个有MAX_LEVEL层级的空节点
# 第二个节点3有2层 第三个节点6有5层 第四个节点7有1层 通过这几个举例应该就能看懂insert方法了
# 打印方法print_skiplist逐層打印層內元素值
# Author: AllenGFLiu
# #####################################################
import random


class ListNode:
    def __init__(self, data=None):
        self._data = data
        self._forwards = []
        self._index = []


class SkipList:
    # 此样例代码只存储整数，并且不重复
    MAX_LEVEL = 16  # 定义一个最大层级数，防止random时出现过大的数据

    def __init__(self):
        self._level_count = 1  # 标识本跳表对象内部实际的最大的层级数,暂时先初始化为0
        self._head = ListNode()
        self._head._forwards = [None] * SkipList.MAX_LEVEL

    def random_level(self, p=0.5):
        level = 1
        while random.random() < p and level < SkipList.MAX_LEVEL:
            level += 1
        return level

    def insert(self, value):
        # 与链表的插入动作原理类似
        level = self.random_level()  # 以random的形式去随机得到新节点插入调表时所拥有的层数(包含数据层和索引层)
        if self._level_count < level:
            self._level_count = level
        
        new_node = ListNode(value)
        new_node._forwards = [None]*level
        new_node._index = [None]*level
        update = [None] * level  # update is similar to a list of prev

        p = self._head
        for i in range(level-1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]

            update[i] = p  # found a prev( prev = self.head if no while loop else p)

        for i in range(level):
            new_node._forwards[i] = update[i]._forwards[i]  # new_node.next = prev.next
            update[i]._forwards[i] = new_node  # pre.next = new_node
            new_node._index[i] = i

    def __repr__(self):
        # 此方法只返回了本跳表的原始链表层数据
        # 不包含在此链表层之上建立的索引层数据
        values = []
        p = self._head
        while p._forwards[0]:
            values.append(str(p._forwards[0]._data))
            p = p._forwards[0]
        return '->'.join(values)
    
    def print_skiplist(self):
        # 此打印方法從最高層逐層打印內部節點_data值
        for i in range(self._level_count-1, -1, -1):
            p = self._head
            values = []
            while p._forwards[i]:
                values.append(str(p._forwards[i]._data))
                p = p._forwards[i]
            print('第'+str(i)+'層', '->'.join(values))

    def find(self, value):
        p = self._head
        for i in range(self._level_count-1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]
        
        return p._forwards[0] and p._forwards[0]._data == value

    def delete(self, value):
        update = [None] * self._level_count
        p = self._head
        for i in range(self._level_count-1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]
            update[i] = p
        
        if p._forwards[0] and p._forwards[0]._data == value:
            for i in range(self._level_count-1, -1, -1):
                if update[i]._forwards[i] and update[i]._forwards[i]._data == value and update[i]._forwards[i]._index[i]:
                    update[i]._forwards[i] = update[i]._forwards[i]._forwards[i]  # similar to prev.next = prev.next.next



if __name__ == '__main__':
    l = SkipList()
    # for i in range(10):
    #     l.insert(i)
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(3)
    l.insert(4)
    l.print_skiplist()
    l.delete(3)
    l.print_skiplist()
    print(l.find(1))
    # print(l)