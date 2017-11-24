

"""
Depth-first search implementation
https://en.wikipedia.org/wiki/Depth-first_search
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

    def dfs(self, source, target=None):
        """ Depth-first search implementation

        Parameters
        ----------
        source : var
                 name of initial node
        target : int, str, optional
                 name of target node

        Returns
        -------
        out : list
              list of visited nodes

        """
        # create visited list and stack
        visited, stack = list(), [source]
        while stack:
            # pop node from stack
            node = stack.pop()
            if node not in visited:
                # add node to visited
                visited.append(node)
                # add child nodes to stack
                stack.extend(self.graph[node])
            if target is not None and node == target:
                break
        return visited

    def dfs_path(self, source, target):
        """ return short path from source node to target """
        dfs_path = self.dfs(source, target)
        if source == target:
            return [source]
        elif len(dfs_path) == 1:
            # path does not found
            return [float('Inf')]
        else:
            if source == dfs_path[0] and target == dfs_path[-1]:
                # correct path
                return dfs_path
            else:
                # path does not found
                return [float('Inf')]

    def dfs_edges(self, source, target):
        """ return minimum number of edges between source node and target """
        dfs_path = self.dfs_path(source, target)
        if dfs_path == [float('Inf')]:
            # path does not found
            return float('Inf')
        return len(dfs_path) - 1

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
        print("dfs path from {} to {} node: {}".format(
            SRC, DEST, GRAPH.dfs_path(SRC, DEST)))
        print("number of edges from {} to {} node: {}".format(
            SRC, DEST, GRAPH.dfs_edges(SRC, DEST)))
