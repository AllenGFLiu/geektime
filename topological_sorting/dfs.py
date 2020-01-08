from directed_graph import DirectedGraph


def dfs(graph):
    def helper(vertex, inverse_adj_table, visited):
        # 遞歸處理逆鄰接表中每個頂點可達的頂點,意味著最後一個頂點是最先被執行(print出來)的
        # 然後再打印自己
        for i in range(len(inverse_adj_table[vertex])):
            w = inverse_adj_table[vertex][i]
            if visited[w]: continue
            visited[w] = True
            helper(w, inverse_adj_table, visited)

        print('->'+str(vertex), end=' ')
        

    # 先構建逆鄰接表 s->t就代表t先於s執行,即s依賴于t
    inverse_adj = [[] for _ in range(graph.v_number)]
    for i in range(graph.v_number):
        for j in range(len(graph.adj_table[i])):
            w = graph.adj_table[i][j]
            inverse_adj[w].append(i)

    visited = [False for _ in range(graph.v_number)]
    for i in range(graph.v_number):
        if not visited[i]:
            visited[i] = True
            helper(i, inverse_adj, visited)
    print()


if __name__ == '__main__':
    graph = DirectedGraph(5)
    graph.add_edge(0,1)
    graph.add_edge(0,3)
    graph.add_edge(1,4)
    graph.add_edge(1,3)
    graph.add_edge(2,1)
    graph.add_edge(2,4)
    dfs(graph)