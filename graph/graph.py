# -*- coding:utf-8 -*-


class UndirectedGraph:
    """无向图的实现
    """
    def __init__(self, vertex_number):
        self.v_number = vertex_number
        self.adj_table = [[] for _ in range(self.v_number)]

    def add_edge(self, s, t):
        '''无向图里建立边的关系需要保存对向的两个顶点的数据
        '''
        if s > self.v_number or t > self.v_number:
            return False
        self.adj_table[s].append(t)
        self.adj_table[t].append(s)
        return True

    # def __getitem__(self, index):
    #     return self.adj_table[index]

    def __repr__(self):
        return str(self.adj_table)


class DirectedGraph:
    """有向图的实现
    """
    def __init__(self, vertex_number):
        self.v_number = vertex_number
        self.adj_table = [[] for _ in range(self.v_number)]

    def add_edge(self, fr, to):
        '''有向图中只保存本顶点指向的顶点信息
        '''
        if fr > self.v_number or to > self.v_number:
            return False
        self.adj_table[fr].append(to)
        return True

    def __repr__(self):
        return str(self.adj_table)

if __name__ == '__main__':
    ug = UndirectedGraph(3)
    ug.add_edge(0, 1)
    ug.add_edge(0, 2)
    print(ug)

    dg = DirectedGraph(3)
    dg.add_edge(0, 1)
    dg.add_edge(0, 2)
    print(dg)