

"""
Breadth-first search implementation
https://en.wikipedia.org/wiki/Breadth-first_search
"""

from __future__ import print_function


class Graph(object):
    """ Simple implementation of Undirected Graph

    graph : dict
            key: node, values: list of connected nodes
    """
    def __init__(self, graph):
        self.graph = graph

    def __str__(self):
        """ string representation of the graph """
        string = ''
        for index, lst in sorted(self.graph.items()):
            strnode = " ".join([str(i) for i in lst])
            string += "node {}: {}\n".format(index, strnode)
        return string[:-1]

    def bfs(self, source, target=None):
        """ Breadth-first search implementation

        Parameters
        ----------
        source : key in graph dict
                 name of initial node
        target : optional
                 name of target node

        Returns
        -------
        out : list
              list of visited nodes

        """
        # create visited list and queue
        visited, queue = list(), [source]
        while queue:
            # popleft node from queue
            node = queue[0]
            del queue[0]
            if node not in visited:
                # add node to visited
                visited.append(node)
                # add nodes to queue
                queue.extend(self.graph[node])
            if target is not None and node == target:
                break
        return visited

    def bfs_path(self, source, target):
        """ breadth-first search path from source to target node """
        bfs_path = self.bfs(source, target)
        if source == target:
            return [source]
        elif len(bfs_path) == 1:
            # path does not found
            return [float('Inf')]
        else:
            if source == bfs_path[0] and target == bfs_path[-1]:
                # correct path
                return bfs_path
            else:
                # path does not found
                return [float('Inf')]

    def bfs_edges(self, source, target):
        """ number of edges from source to target node """
        bfs_path = self.bfs_path(source, target)
        if bfs_path == [float('Inf')]:
            # path does not found
            return float('Inf')
        return len(bfs_path) - 1

if __name__ in '__main__':
    GRAPH_DATA = {'A': ['B', 'C', 'E'],
                  'B': ['A', 'D', 'E'],
                  'C': ['A', 'F', 'G'],
                  'D': ['B'],
                  'E': ['A', 'B', 'D'],
                  'G': ['C'],
                  'F': ['C'],
                  'H': [],
                  'J': ['K', 'M'],
                  'K': ['M'],
                  'M': ['K']}
    GRAPH = Graph(GRAPH_DATA)
    print("Show Graph:\n{}\n".format(GRAPH))
    for SRC, DEST in [('A', 'G'), ('G', 'B'), ('H', 'A'), ('D', 'D')]:
        print("The bfs path from {} to {} node: {}".format(
            SRC, DEST, GRAPH.bfs_path(SRC, DEST)))
        print("number of edges from {} to {} node: {}".format(
            SRC, DEST, GRAPH.bfs_edges(SRC, DEST)))
