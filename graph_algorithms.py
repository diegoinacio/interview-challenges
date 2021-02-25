class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def add_neighbor(self, n, w=0):
        self.adjacent[n] = w

class UndirectedGraph:
    def __init__(self):
        self.vertices = {}
        self.n_vert = 0

    def add_vertex(self, vertex):
        self.n_vert += 1
        self.vertices[vertex] = Vertex(vertex)

    def add_edge(self, vo, vi, w=0):
        if vo not in self.vertices:
            self.add_vertex(vo)
        if vi not in self.vertices:
            self.add_vertex(vi)
        self.vertices[vo].add_neighbor(self.vertices[vi], w)
        self.vertices[vi].add_neighbor(self.vertices[vo], w)

    def get_vertex(self, vertex):
        adjacent = self.vertices[vertex].adjacent
        n_vert = len(adjacent)
        return [
            vertex,
            n_vert,
            {v.id: adjacent[v] for v in adjacent}
        ]

    def get_vertices(self):
        return [self.get_vertex(v) for v in sorted(self.vertices)]

    def display_vertex(self, vertex):
        Vertex = self.get_vertex(vertex)
        n_vert = Vertex[1]
        adjacent = Vertex[2]
        output = f'[{n_vert}] Vertex "{vertex}":\n'
        for v in sorted(adjacent):
            output += f'\t{vertex} <-> {v} [{adjacent[v]}]\n'
        print(output)

    def display_vertices(self):
        for vertex in self.vertices.keys():
            self.display_vertex(vertex)
