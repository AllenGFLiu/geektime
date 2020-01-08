class DirectedGraph:
    def __init__(self, vertex_number):
        self.v_number = vertex_number
        self.adj_table = [[] for _ in range(vertex_number)]
        self.count = 0


    def add_edge(self, s, t):
        if self.count == self.v_number:
            return

        self.count += 1
        self.adj_table[s].append(t)