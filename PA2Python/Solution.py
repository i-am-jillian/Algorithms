from collections import deque
class Solution:

    def __init__(self, start_node, graph):
        self.start_node = start_node
        self.graph = graph

    def output_distances(self):
        """
        :return: the list of minimum distances from each node to the start node
        """
        #find the number of nodes in the graph
        nodes = len(self.graph)
        #initialize list of distances with -1
        distance = [-1] * nodes
        #setting start node at position 0
        distance[self.start_node] = 0
        
        #adding the start node in the queue
        queue = deque([self.start_node])

        #traversing the graph by taking the node that im standing on and check its neighbors
        while queue:
            current = queue.popleft()
            for neighbors in self.graph.get(current,[]):
                #checking for nodes that are not visited yet (-1)
                if distance[neighbors] ==  -1:
                    #set their distance in distance list
                    distance[neighbors] = distance[current] + 1
                    #append the node to the queueu
                    queue.append(neighbors)

        return distance
