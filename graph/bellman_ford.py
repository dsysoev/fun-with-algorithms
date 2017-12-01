

"""
Implementation of Bellman Ford algorithm
https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
"""

from __future__ import print_function


def bellman_ford(nodes, edges, source):
    """
    Bellman ford shortest path algorithm

    Parameters
    ----------
    nodes : set
            names of all nodes in the graph
    egdes : list
            list of dependencies between nodes in the graph
            [(node1, node2, weight), ...]
    source : str
            name of source node

    Returns
    -------
    out : (bool, dict)
          (has_cycle, distances) has_cycle var check if cycle in the graph
          distance dict show len from source node to all nodes in the graph

    """
    # initialize distance to every node as infinity
    distances = {node: float('Inf') for node in nodes}
    # set distance to source node as zero
    distances[source] = 0
    # repeat n-1 times
    for _ in range(1, len(nodes)):
        # iterate over every edge
        for src, dest, weight in edges:
            if distances[dest] > distances[src] + weight:
                # relax
                distances[dest] = distances[src] + weight
    has_cycle = False
    for src, dest, weight in edges:
        if distances[dest] > distances[src] + weight:
            # If a node can still be relaxed,
            # it means that there is a negative cycle
            has_cycle = True
    return has_cycle, distances

if __name__ in '__main__':
    GRAPH_NODES = {'s', 't', 'y', 'x', 'z', 'm'}
    GRAPH_DEPENDECIES = [('s', 't', 6), ('s', 'y', 7), ('t', 'x', 5),
                         ('x', 't', -2), ('t', 'y', 8), ('y', 'z', 9),
                         ('y', 'x', -3), ('t', 'z', -4), ('z', 's', 2),
                         ('z', 'x', 7)]
    print(bellman_ford(GRAPH_NODES, GRAPH_DEPENDECIES, 's'))
