INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    dist = [[INF] * n for _ in range(n)]
    
    # Initialize distances with the given graph
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
    
    # Update distances using Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    return dist

# Example usage
graph = [
    [0, 15, INF, 10],
    [23, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, 1, INF, 0]
]

result = floyd_warshall(graph)
for row in result:
    print(row)
