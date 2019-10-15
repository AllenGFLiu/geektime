# -*- coding:utf-8 -*-
# 使用开放地址法(线性探测)实现的简单的哈希表


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