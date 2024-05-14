class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        self.parent[root1] = root2

def kruskal(graph):
    minimum_spanning_tree = []
    disjoint_set = DisjointSet(graph['vertices'])
    edges = sorted(graph['edges'], key=lambda x: x[2])
    for edge in edges:
        vertex1, vertex2, weight = edge
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            minimum_spanning_tree.append(edge)
            disjoint_set.union(vertex1, vertex2)
    return minimum_spanning_tree

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
    'edges': [
        ('A', 'B', 17),
        ('A', 'D', 15),
        ('B', 'C', 18),
        ('B', 'D', 19),
        ('B', 'E', 17),
        ('C', 'E', 15),
        ('D', 'E', 15),
        ('D', 'F', 16),
        ('E', 'F', 18),
    ]
}

minimum_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)

total_weight = sum(weight for _, _, weight in minimum_spanning_tree)
print("Total weight of the minimum spanning tree is:", total_weight)
