from dataclasses import dataclass
from queue import PriorityQueue


@dataclass
class Edge:
    start_id: int
    end_id: int
    weight: int


@dataclass
class Vertex:
    vertex_id: int
    x: int
    y: int
    f = float('inf')
    distance = float('inf')


class Graph:

    REMOVED = '<entry_removed>'

    def __init__(self, vertex_number):
        self._v_number = vertex_number
        self._adj_table = [[] for _ in range(vertex_number)]
        self._entry_finder = {}
        self._vertexes = [None] * vertex_number

    def add_edge(self, s, t, w):
        self._adj_table[s].append(Edge(s, t, w))

    def add_vertex(self, id, x, y):
        self._vertexes[id] = Vertex(id, x, y)

    def h_manhattan(self, vertex_one, vertex_two):
        return abs(vertex_one.x - vertex_two.x) + abs(vertex_one.y - vertex_two.y)

    def update_priorityqueue(self, vertex_id):
        poped = self._entry_finder.pop(vertex_id)
        poped[-1] = Graph.REMOVED
    
    def print(self, predecessor, to_vertex, from_vertex):
        path = lambda x : path(predecessor[x]) + [str(x)] if x != from_vertex else [str(from_vertex)]

        print('->'.join(path(to_vertex)))
    
    def astar(self, from_vertex, to_vertex):
        predecessor = [-1] * self._v_number
        visited = [False] * self._v_number

        q = PriorityQueue()
        
        self._vertexes[from_vertex].distance = 0
        self._vertexes[from_vertex].f = 0
        visited[from_vertex] = True

        entry = [self._vertexes[from_vertex].f, self._vertexes[from_vertex]]
        q.put(entry)
        self._entry_finder[from_vertex] = entry

        while not q.empty():
            min_vertex = q.get()[-1]
            if min_vertex is not Graph.REMOVED:
                del self._entry_finder[min_vertex.vertex_id]
                for edge in self._adj_table[min_vertex.vertex_id]:
                    next_vertex = self._vertexes[edge.end_id]
                    if min_vertex.distance + edge.weight < next_vertex.distance:
                        next_vertex.distance = min_vertex.distance + edge.weight
                        next_vertex.f = next_vertex.distance + self.h_manhattan(next_vertex, self._vertexes[to_vertex])

                        predecessor[next_vertex.vertex_id] = min_vertex.vertex_id
                        entry = [next_vertex.f, next_vertex]
                        if not visited[next_vertex.vertex_id]:
                            visited[next_vertex.vertex_id] = True
                        else:
                            self.update_priorityqueue(next_vertex.vertex_id)
                        q.put(entry)
                        self._entry_finder[next_vertex.vertex_id] = entry

                    if next_vertex.vertex_id == to_vertex:
                        self.print(predecessor, to_vertex, from_vertex)
                        return


if __name__ == '__main__':
    graph = Graph(11)
    graph.add_vertex(0, 32, 63)
    graph.add_vertex(1, 30, 63)
    graph.add_vertex(2, 28, 62.5)
    graph.add_vertex(3, 26, 63)
    graph.add_vertex(4, 32, 70)
    graph.add_vertex(5, 36, 62)
    graph.add_vertex(6, 32, 59)
    graph.add_vertex(7, 37, 58)
    graph.add_vertex(8, 35, 73)
    graph.add_vertex(9, 39, 69)
    graph.add_vertex(10, 40, 62)
    graph.add_edge(0, 1, 20)
    graph.add_edge(1, 2, 20)
    graph.add_edge(2, 3, 10)
    graph.add_edge(0, 4, 60)
    graph.add_edge(0, 5, 60)
    graph.add_edge(0, 6, 60)
    graph.add_edge(6, 7, 70)
    graph.add_edge(4, 8, 50)
    graph.add_edge(5, 8, 70)
    graph.add_edge(5, 9, 80)
    graph.add_edge(5, 10, 50)
    graph.add_edge(8, 9, 50)
    graph.add_edge(9, 10, 60)
    graph.astar(0, 10)