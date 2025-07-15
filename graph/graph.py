class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        str_graph = ""
        for key, value in self.adj_list.items():
            str_graph += f"{key} -> {value}\n"
        return str_graph

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists!")

    def add_edge(self, source_node, destination_node, weighted=None):
        if source_node not in self.adj_list:
            self.add_node(source_node)
        if destination_node not in self.adj_list:
            self.add_node(destination_node)

        # Add edge (unweighted or weighted)
        if weighted is None:
            self.adj_list[source_node].add(destination_node)
            if not self.directed:
                self.adj_list[destination_node].add(source_node)
        else:
            self.adj_list[source_node].add((destination_node, weighted))
            if not self.directed:
                self.adj_list[destination_node].add((source_node, weighted))

    def obtain_neighbours(self, key_node):
        return self.adj_list.get(key_node, set())

    def dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_node)
        print(start_node, end=' ')

        for neighbor in self.obtain_neighbours(start_node):
            # If it's a weighted graph, neighbor might be a tuple
            if isinstance(neighbor, tuple):
                neighbor = neighbor[0]
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        visited.add(start_node)

        while queue:
            current = queue.pop(0)
            print(current, end=' ')

            for neighbor in self.obtain_neighbours(current):
                if isinstance(neighbor, tuple):
                    neighbor = neighbor[0]
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def adj_matrix(self):
        # Optional: implement adjacency matrix here
        pass


# --- DEMO ---
if __name__ == '__main__':
    graph_obj = Graph()

    graph_obj.add_edge("A", "B")
    graph_obj.add_edge("A", "C")
    graph_obj.add_edge("B", "D")
    graph_obj.add_edge("C", "D")
    graph_obj.add_edge("D", "E")

    print("Graph (Adjacency List):")
    print(graph_obj)

    print("\nDFS from A:")
    graph_obj.dfs("A")

    print("\n\nBFS from A:")
    graph_obj.bfs("A")
