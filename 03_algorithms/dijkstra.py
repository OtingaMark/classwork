import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Distance to start is 0

    # Priority queue to process nodes with the smallest known distance
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # If this path is longer than what we already know, skip it
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            # If a shorter path to neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


# ✅ Sample Graph as an adjacency list
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('E', 3)],
    'D': [('F', 11)],
    'E': [('D', 4)],
    'F': []
}

# Run the algorithm
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

# Print the results
print(f"Shortest paths from node '{start_node}':")
for node, distance in shortest_paths.items():
    print(f" - to {node}: {distance}")
