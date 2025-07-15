class Graphs:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        str_graph = ""
        for key, value in self.adj_list.items():
            str_graph += f"{key} -> {value}\n"
        return str_graph.strip()

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists in the graph.")

    def add_edge(self, source_node, destination_node, weighted=None):
        if source_node not in self.adj_list:
            self.add_node(source_node)
        if destination_node not in self.adj_list:
            self.add_node(destination_node)

        if weighted is not None:
            self.adj_list[source_node].add((destination_node, weighted))
            if not self.directed:
                self.adj_list[destination_node].add((source_node, weighted))
        else:
            self.adj_list[source_node].add(destination_node)
            if not self.directed:
                self.adj_list[destination_node].add(source_node)

    def get_neighbours(self, node):
        return self.adj_list.get(node, set())

    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbours = self.get_neighbours(node)
                for neighbour in sorted(neighbours, reverse=True):
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        stack.append(neighbour)
        return order

    def bfs(self, start):
        visited = set()
        queue = [start]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbours = self.get_neighbours(node)
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        queue.append(neighbour)
        return order

    def adj_matrix(self):
        print("Adjacency Matrix not yet implemented.")


# MAIN BLOCK
if __name__ == "__main__":
    graph = Graphs(directed=False)
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_edge("A", "B", weighted=2)
    graph.add_edge("A", "C")
    graph.add_edge("B", "C", weighted=5)

    print("Graph structure:\n", graph)
    print("\nBFS starting from A:", graph.bfs("A"))
    print("DFS starting from A:", graph.dfs("A"))
