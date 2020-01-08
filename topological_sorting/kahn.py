from directed_graph import DirectedGraph
from collections import deque


# 有向圖中,定義s指向t代表s先於t執行,即t依賴s
def kahn(graph):
    in_degree = [0 for _ in range(graph.v_number)]
    for to_vertexs in graph.adj_table:
        for to_vertex in to_vertexs:
            in_degree[to_vertex] += 1

    q = deque()
    for index, count in enumerate(in_degree):
        if count == 0:
            q.append(index)

    while q:
        i = q.popleft()
        print('->'+str(i), end=' ')
        for j in range(len(graph.adj_table[i])):
            k = graph.adj_table[i][j]
            in_degree[k] -= 1
            if in_degree[k] == 0:
                q.append(k)
    print()

if __name__ == '__main__':
    graph = DirectedGraph(5)
    graph.add_edge(0,1)
    graph.add_edge(0,3)
    graph.add_edge(1,4)
    graph.add_edge(1,3)
    graph.add_edge(2,1)
    graph.add_edge(2,4)

    kahn(graph)

