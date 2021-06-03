class Vertex {
  constructor(node) {
    this.id = node;
    this.adjacent = {};
  }

  add_neighbor(n, w = 0) {
    this.adjacent[n.id] = w;
  }
}

class UndirectedGraph {
  constructor() {
    this.vertices = {};
    this.n_vert = 0;
  }

  add_vertex(vertex) {
    this.vertices[vertex] = new Vertex(vertex);
    this.n_vert += 1;
  }

  add_edge(vo, vi, w = 0) {
    if (!(vo in this.vertices)) {
      this.add_vertex(vo);
    }
    if (!(vi in this.vertices)) {
      this.add_vertex(vi);
    }
    this.vertices[vo].add_neighbor(this.vertices[vi], w);
    this.vertices[vi].add_neighbor(this.vertices[vo], w);
  }

  get_vertex(vertex) {
    const adjacent = this.vertices[vertex].adjacent;
    const n_vert = Object.keys(adjacent).length;
    return [vertex, n_vert, adjacent];
  }

  get_vertices() {
    return Object.keys(this.vertices)
      .sort()
      .map((v) => this.get_vertex(v));
  }

  display_vertex(vertex) {
    const VERTEX = this.get_vertex(vertex);
    const n_vert = VERTEX[1];
    const adjacent = VERTEX[2];
    let output = `[${n_vert}] Vertex "${vertex}":\n`;
    Object.keys(adjacent)
      .sort()
      .forEach((v) => {
        output += `\t${vertex} <-> ${v} [${adjacent[v]}]\n`;
      });
    console.log(output);
    return "ok";
  }

  display_vertices() {
    Object.keys(this.vertices)
      .sort()
      .forEach((vertex) => {
        this.display_vertex(vertex);
      });
    return "ok";
  }
}

module.exports = {
  UndirectedGraph,
};
