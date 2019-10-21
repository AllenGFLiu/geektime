# -*- coding:utf-8 -*-
import random


class ListNode:
    def __init__(self, data=None):
        self._data = data
        self._forwards = []


class SkipList:

    MAX_LEVEL = 16

    def __init__(self):
        self._level_count = 1
        self._head = ListNode()
        self._head._forwards = [None] * SkipList.MAX_LEVEL

    def random_level(self, p=0.5):
        level = 1
        while random.random() < p and level < SkipList.MAX_LEVEL:
            level += 1
        return level

    def insert(self, value):
        level = self.random_level()
        if self._level_count < level:
            self._level_count = level
        
        new_node = ListNode(value)
        new_node._forwards = [None]*level
        update = [self._head] * level

        p = self._head
        for i in range(level-1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]

            update[i] = p

        for i in range(level):
            new_node._forwards[i] = update[i]._forwards[i]
            update[i]._forwards[i] = new_node

    def __repr__(self):
        values = []
        p = self._head
        while p._forwards[0]:
            values.append(str(p._forwards[0]._data))
            p = p._forwards[0]
        return '->'.join(values)

if __name__ == '__main__':
    l = SkipList()
    for i in range(10):
        l.insert(i)
    print(l)