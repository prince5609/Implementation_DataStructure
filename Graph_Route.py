class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph_dict :", self.graph_dict)

    def get_paths(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for i in new_paths:
                    paths.append(i)
        return paths

    def get_shortest_path(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return []

        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    route_graph = Graph(routes)

    start1 = "Mumbai"
    end1 = "Mumbai"
    print("Route from Mumbai to Mumbai :", route_graph.get_paths(start1, end1))

    start2 = "Toronto"
    end2 = "Mumbai"
    print("Route from Toronto to Mumbai :", route_graph.get_paths(start2, end2))

    start3 = "Mumbai"
    end3 = "New York"
    print("Routes fro Mumbai To New York :", route_graph.get_paths(start3, end3))

    start4 = "Toronto"
    end4 = "Mumbai"
    print(f"Shortest path from {start4} to {end4} :", route_graph.get_shortest_path(start4, end4))

    start5 = "New York"
    end5 = "New York"
    print(f"Shortest path from {start5} to {end5} :", route_graph.get_shortest_path(start5, end5))

    start6 = "Mumbai"
    end6 = "New York"
    print(f"Shortest path from {start6} to {end6} :", route_graph.get_shortest_path(start6, end6))
