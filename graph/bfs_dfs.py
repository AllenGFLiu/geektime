# -*-: coding:utf-8 -*-
from collections import deque
from graph import UndirectedGraph


def print_path(fr, to, prev):
    '''yield from Iterable = for value in Iterable : yield value 
    '''
    if prev[fr] or fr != to:
        yield from print_path(fr, prev[to], prev)
    yield str(to)


def bfs(graph_object, fr, to):
    '''base on UndirectedGraph
    find the path from Vertex fr to Vertex to,using bfs
    visited:用来记录顶点是否已经被访问
    queue:用来存储已经被访问，但相连的顶点还没有被访问的顶点
    prev:用来记录搜索路径，不过是反向存储的，prev[3]=2就是说从顶点2到达的顶点3，
        所以需要使用递归来打印所有路径。
    '''
    if fr == to: return
    visited = [False] * graph_object.v_number
    visited[fr] = True

    q = deque()
    q.append(fr)
    prev = [None] * graph_object.v_number

    while q:
        v = q.popleft()
        for related in graph_object[v]:
            if not visited[related]:
                prev[related] = v
                if related == to:
                    print('->'.join(print_path(fr, to, prev)))
                    return
                visited[related] = True
                q.append(related)


def dfs(graph_object, fr, to):
    '''base on UndirectedGraph
    find the path from Vertex fr to Vertex to, using dfs
    '''
    found = False
    visited = [False] * graph_object.v_number
    prev = [None] * graph_object.v_number

    def _dfs(from_vertex):
        nonlocal found
        if found : return
        visited[from_vertex] = True
        if from_vertex == to:
            found = True
            return
        for related in graph_object[from_vertex]:
            if found: return
            if not visited[related]:
                prev[related] = from_vertex
                _dfs(related)

    _dfs(fr)
    print('->'.join(print_path(fr, to, prev)))


if __name__ == '__main__':
    ug = UndirectedGraph(8)
    ug.add_edge(0, 1)
    ug.add_edge(0, 3)
    ug.add_edge(1, 2)
    ug.add_edge(1, 4)
    ug.add_edge(2, 5)
    ug.add_edge(3, 4)
    ug.add_edge(4, 5)
    ug.add_edge(4, 6)
    ug.add_edge(5, 7)
    ug.add_edge(6, 7)
    bfs(ug, 0, 7)
    dfs(ug, 0, 7)





