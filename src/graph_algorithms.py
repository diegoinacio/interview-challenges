class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def add_neighbor(self, n, w=0):
        self.adjacent[n.id] = w


class UndirectedGraph:
    def __init__(self):
        self.vertices = {}
        self.n_vert = 0

    def add_vertex(self, vertex):
        self.vertices[vertex] = Vertex(vertex)
        self.n_vert += 1

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
        return [vertex, n_vert, adjacent]

    def get_vertices(self):
        return [self.get_vertex(v) for v in sorted(self.vertices)]

    def display_vertex(self, vertex):
        VERTEX = self.get_vertex(vertex)
        n_vert = VERTEX[1]
        adjacent = VERTEX[2]
        output = f'[{n_vert}] Vertex "{vertex}":\n'
        for v in sorted(adjacent):
            output += f'\t{vertex} <-> {v} [{adjacent[v]}]\n'
        print(output)
        return "ok"

    def display_vertices(self):
        for vertex in sorted(self.vertices.keys()):
            self.display_vertex(vertex)
        return "ok"
