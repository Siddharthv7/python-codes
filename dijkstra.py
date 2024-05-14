import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

graph = {
    'A': {'B': 13, 'C': 14},
    'B': {'A': 13, 'C': 22, 'D': 15},
    'C': {'A': 14, 'B': 22, 'D': 11},
    'D': {'B': 15, 'C': 11}
}

start_node = 'A'
print("Shortest distances:", dijkstra(graph, start_node))
