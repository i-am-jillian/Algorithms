import sys

class Solution:

    def __init__(self, graph):
        self.graph = graph

    def output_edges(self):
        ########### Output the node ids of the smallest weighted path ############
        #initializing arrays
        length = len(self.graph) #getting the lenght of the graph
        parent = [-1] * length #setting placeholders for every parent node to -1
        weight = [float('inf')] * length #setting placeholder for all weights to infinity
        visited = [False] * length #keeping track of visited nodes

        weight[0] = 0 #starting from node 0

        #iterating graoh
        for _ in range(length):
            u = -1;
            min = float('inf')

            for i in range(length):
                if not visited[i] and weight[i]<min:
                    min = weight[i]
                    u = i
            if u == -1:
                break

            visited[u] = True

            for v in range(length):
                weight = self.graph[u],[v]

                if weight != -1 and not visited[v] and weight < weight[v]:
                    weight[v] = weight
                    parent[v] = u
 
        return parent
