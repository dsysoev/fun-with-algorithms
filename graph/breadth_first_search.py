

"""
Breadth-first search implementation
https://en.wikipedia.org/wiki/Breadth-first_search
"""

from __future__ import print_function

import queue


class Graph(object):
    """ Simple implementation of Undirected Graph

    graph : list of lists
            list of pairs of connected edges
    """
    def __init__(self, graph):
        self.graph = graph

    def __str__(self):
        """ string representation of Graph """
        string = ''
        for index, lst in sorted(self.graph.items()):
            strnode = " ".join([str(i) for i in lst])
            string += "node {}: {}\n".format(index, strnode)
        return string[:-1]

    def BFS(self, source):
        """ Breadth-first search implementation

        Parameters
        ----------

        source : int
                 number of initial node

        Returns
        -------

        out : (list, list)
              The tuple (distance, paths) for each node

        """
        unique = []
        for node, lst in self.graph.items():
            unique.append(node)
            unique.extend(lst)
        # create set of unique nodes
        unique = set(unique)
        # palette: 0 - WHITE, 1 - GRAY, 2 - BLACK
        color = {k: 0 for k in unique}
        # set black color for source node
        color[source] = 2
        distance = {k: float('Inf') for k in unique}
        # set zero distance for source node
        distance[source] = 0
        # set infinite for all paths by default
        paths = {k: [] for k in unique}
        # set init queue
        queue_ = queue.Queue()
        # enqueue source node
        queue_.put(source)
        while not queue_.empty():
            node = queue_.get()
            # use get method for node which does not presented in graph
            for current in self.graph.get(node, []):
                if color[current] == 0:
                    # color is white
                    # set gray color
                    color[current] = 1
                    # apply distance
                    distance[current] = distance[node] + 1
                    # add node path and current name to current node
                    paths[current].extend(paths[node])
                    paths[current].append(current)
                    # enqueue current node
                    queue_.put(current)
            # set black color for node
            color[node] = 2
        # set [None] for source node
        paths[source] = [None]
        for index, node in paths.items():
            if node == []:
                # set paths as infinite
                paths[index] = [float('Inf')]
        return distance, paths

    def get_short_path(self, source, target):
        """ return short path from source node to target """
        _, paths = self.BFS(source)
        return paths[target]

    def get_num_edges(self, source, target):
        """ return minimum number of edges between source node and target """
        distance, _ = self.BFS(source)
        return distance[target]

if __name__ in '__main__':
    GRAPH_DATA = {'A': ['B', 'C', 'E'],
                  'B': ['A', 'D', 'E'],
                  'C': ['A', 'F', 'G'],
                  'D': ['B'],
                  'E': ['A', 'B', 'D'],
                  'G': ['C'],
                  'H': []}
    GRAPH = Graph(GRAPH_DATA)
    print("Show Graph:\n{}\n".format(GRAPH))

    for SRC, DEST in [('A', 'F'), ('G', 'B'), ('H', 'A'), ('D', 'D')]:
        print("The shortest path from {} to {} node: {}".format(
            SRC, DEST, GRAPH.get_short_path(SRC, DEST)))
        print("Minimun number of edges from {} to {} node: {}".format(
            SRC, DEST, GRAPH.get_num_edges(SRC, DEST)))
