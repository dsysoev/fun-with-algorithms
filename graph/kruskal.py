

"""
Kruskal's algorithm
https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
"""

from __future__ import print_function


class Graph(object):
    """ Simple implementation of directed acyclic graph

    Parameters
    ----------
    nodes : set
            set of all nodes in the graph
    dependencies : list
            list of tuples (weight, node1, node2) which show connection
            between nodes of the graph with appropriate weight
    """
    def __init__(self, nodes, dependencies):
        self.nodes = nodes
        self.dependencies = dependencies
        self.parent = {}
        self.rank = {}

    def __str__(self):
        """ string representation of the graph """
        string = ''
        for node in sorted(self.nodes):
            strnode = ["{} -> {} ({})".format(start, end, w)
                       for w, start, end in self.dependencies if start == node]
            string += "node {}: {}\n".format(node, " ".join(strnode))
        return string[:-1]

    def find(self, edge):
        """ for current edge return parent edge """
        if self.parent[edge] != edge:
            self.parent[edge] = self.find(self.parent[edge])
        return self.parent[edge]

    def union(self, edge1, edge2):
        """ union edge1 and edge2 into one tree """
        root1 = self.find(edge1)
        root2 = self.find(edge2)
        if root1 == root2:
            return
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1

    def minimum_spanning_tree(self):
        """ a minimum spanning tree

        Returns
        -------
        out : set
              return a set of tuples (weight, node1, node2)
              with minimum spanning tree for a connected weighted graph

        """
        # make_set
        self.parent = {node: node for node in self.nodes}
        self.rank = {node: 0 for node in self.nodes}
        # sort edges
        # weight should be first item in tuple
        edges = self.dependencies
        edges.sort()
        # set initial tree
        minimum_spanning_tree = set()
        for weight, edge1, edge2 in edges:
            if self.find(edge1) != self.find(edge2):
                # union edge1 and edge2
                self.union(edge1, edge2)
                # add new dependence to the tree
                minimum_spanning_tree.add((weight, edge1, edge2))

        return minimum_spanning_tree

if __name__ in '__main__':
    GRAPH_NODES = {0, 1, 2, 3, 4, 5, 6, 7}
    # [(weight, node1, node2), ...]
    GRAPH_DEPENDECIES = [(4, 0, 4), (7, 4, 2), (6, 2, 6), (8, 0, 1),
                         (3, 1, 5), (7, 5, 7), (6, 5, 6), (8, 5, 2)]
    GRAPH = Graph(GRAPH_NODES, GRAPH_DEPENDECIES)
    print("Show graph:\n{}\n".format(GRAPH))
    print("Minimum spanning tree: {}".format(GRAPH.minimum_spanning_tree()))
