"""
Undirected Graph: There is no direction for Nodes
Directed Graph : Nodes have Connection
One application Example: Facebook Friend Suggestion, Flight Routes
Different from a Tree: In A tree there is only one path between two Nodes
Google maps uses Graphs to guide you to desired place to move to
"""
#Initializing a Graph Class
class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
               self.graph_dict[start] = [end] 
        print("Graph Dictionary",self.graph_dict)
    
    def get_paths(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node,end,path)
                for p in new_path:
                    paths.append(p)

        return paths
    def get_shortest_path(self,start,end,path = []):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return None  
        short_path = None 
        for node in self.graph_dict[start]:
            if node not in path:  
                sp = self.get_shortest_path(node,end,path) 
                if sp:
                    if short_path is None or len(sp) < len(short_path):
                        short_path = sp


        return short_path   






if __name__ == "__main__":
    routes =[
        ("Kigali","Paris"),
        ("Kigali", "Dubai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Dubai","New York"),
        ("New York", "Toronto")
    ]

    rutes_graph = Graph(routes)
    start = "Kigali"
    end = "New York"

    print(f"The Path Between {start} and {end} is: ", rutes_graph.get_paths(start,end))
    print(f"The Shortest Path Between {start} and {end} is: ", rutes_graph.get_shortest_path(start,end))

