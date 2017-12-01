

"""
Dijkstra's algorithm implementation
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""

from __future__ import print_function


def dijkstra(edges, source, target):
    """ Dijkstra's algorithm

    The weight between nodes should have positive value

    Parameters
    ----------
    edges : list of tuples
            list of dependencies between nodes in the graph
            [(source, target, weight), ...]
    source : str
            name of source node of the graph
    target : str
            name of target node of the graph

    Returns
    -------
    out : tuple
          length and path between source and target node
          tuple (length, path)

    """
    graph = {}
    # determine the dict
    # where key - source node and
    # items - list of [(weight, destination), ...]
    for src, dest, weight in edges:
        if src not in graph:
            graph[src] = []
        graph[src].append((weight, dest))
    # set a queue
    # weight, source node, path
    queue = [(0, source, ())]
    # initialize visited
    visited = set()
    while queue:
        # get item from queue
        cost, src, path = queue.pop()
        if src not in visited:
            # this is a new node
            visited.add(src)
            # add src node to the path
            path = (path, src)
            if src == target:
                # target node was reached
                return cost, path
            # loop for all connected nodes to src node
            for weight, dest in graph.get(src, ()):
                if dest not in visited:
                    # we find new way
                    # add to the queue
                    queue.insert(0, (cost + weight, dest, path))
    return float("inf"), ()

if __name__ == "__main__":
    EDGES = [
        ('s', 't', 6),
        ('s', 'y', 7),
        ('t', 'x', 5),
        ('x', 't', -2),
        ('t', 'y', 8),
        ('y', 'z', 9),
        ('y', 'x', -3),
        ('t', 'z', -4),
        ('z', 's', 2),
        ('z', 'x', 7)
    ]
    for SRC, DEST in [('s', 'z'), ('a', 'z'), ('s', 's')]:
        LEN, PATH = dijkstra(EDGES, SRC, DEST)
        print("Length of the path from '{}' to '{}' = {}".format(SRC, DEST, LEN))
        print("Path from '{}' to '{}': {}".format(SRC, DEST, PATH))
