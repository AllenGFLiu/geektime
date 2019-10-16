# -*- coding:utf-8 -*-
# 使用开放地址法(线性探测)实现的简单的哈希表 Hash
# 增添负载因子，当哈希表内数量超过因子值，自动启动扩充并搬移数据 DynamicHash


class Hash:
    def __init__(self):
        # 定死的表长度为11
        self.hash_table = [[None, None] for i in range(11)]

    def hash(self, k, i):
        h_value = (k+i)%11
        if self.hash_table[h_value][0] == k:
            return h_value
        if self.hash_table[h_value][0] != None:
            i += 1
            h_value = self.hash(k, i)
        return h_value

    def put(self, k, v):
        hash_v = self.hash(k, 0)
        self.hash_table[hash_v][0] = k
        self.hash_table[hash_v][1] = v

    def get(self, k):
        hash_v = self.hash(k, 0)
        return self.hash_table[hash_v][1]


class DynamicHash:
    def __init__(self):
        self.capacity = 11
        self.hash_table = [[None, None] for in range(self.capcacity)]
        self.num = 0
        self.load_factor = 0.75

    def hash(self, k, i):
        h_value = (k+i)%self.capacity
        if self.hash_table[h_value][0] == k:
            return h_value
        if self.hash_table[h_value][0] != None:
            i += 1
            h_value = self.hash(k, i)
        return h_value

    def push(self, k, v):
        hash_v = self.hash(k, 0)
        self.hash_table[hash_v][0] = k
        self.hash_table[hash_v][1] = v
        self.num += 1
        if (self.num/self.capacity) > self.load_factor:
            self.resize()

    def resize(self):
        self.capacity *= 2
        temp_table = self.hash_table[:]
        self.hash_table = [[None, None] for i in range(self.capacity)]
        for value in temp_table:
            if value[0]:
                hash_v = self.hash(value[0], 0)
                self.hash_table[hash_v][0] = value[0]
                self.hash_table[hash_v][1] = value[1]

    def get(self, k):
        hash_v = self.hash(k, 0)
        return self.hash_table[hash_v][1]