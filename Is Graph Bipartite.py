'''
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split its set of nodes 
into two independent subsets A and B, such that every edge in the
 graph has one node in A and another node in B.

The graph is given in the following form: graph[i] 
is a list of indexes j for which the edge between nodes 
i and j exists. Each node is an integer between 0 and graph.
length - 1. There are no self edges or parallel edges: graph[i]
 does not contain i, and it doesn't contain any element twice.
'''
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        c = {}
        for node in range(len(graph)):
            if node in c:  
                continue
            c[node] = 1
            queue = [node]
            for p in queue:
                for n in graph[p]:
                    if n not in c:
                        c[n] = -c[p]
                    elif c[n] == c[p]:
                        return False
                    if n not in queue:
                        queue.append(n)
        return True