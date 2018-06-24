

"""
Dijkstra's algorithm implementation
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""

from __future__ import print_function


def dijkstra(edges, source, target):
    """ Dijkstra's algorithm

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
    # determine the graph as dict where:
    # key - source node and
    # item - list of [(destination, weight), ...]
    graph = {}
    for src, dest, weight in edges:
        if src not in graph:
            graph[src] = []
        graph[src].append((dest, int(weight)))
    # set a queue
    # weight, source node, path from source node
    queue = [(0, source, [source])]
    # initialize visited nodes
    # visited nodes - nodes with a known shortest path
    # key - visited node
    # item - (cost, path)
    visited = dict()

    while queue:
        # get item from queue
        cost, src, path = queue.pop()
        if src not in visited:
            # this is a new visited node
            visited[src] = (cost, path)

        if src == target:
            # target node was reached
            return cost, path

        # set initial weight, destination node and path
        min_weight, min_dest, min_path = float('Inf'), None, None
        # loop for all visited nodes
        for src_, (cost_, path_) in visited.items():
            # find a shortest path
            # from src node to the nearest node
            for dest, weight in graph.get(src_, ()):
                if dest in visited:
                    # skip nodes with a known shortest path
                    continue
                # calculate current cost
                current_cost = cost_ + weight
                if current_cost < min_weight:
                    min_weight, min_dest, min_path = current_cost, dest, path_

        if min_dest is not None:
            # we find shortest path to new node
            # shortest path was updated
            path = min_path + [min_dest]
            # add to the queue
            queue.insert(0, (min_weight, min_dest, path))

    # Return infinity if the target node is not reached
    return float('Inf'), []

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
    for SRC, DEST, MINLEN in [
        ('s', 'z', 2), ('a', 'z', float('Inf')), ('s', 's', 0)]:
        
        LEN, PATH = dijkstra(EDGES, SRC, DEST)
        print("Length of the path from '{}' to '{}' = {}, ({})"
            .format(SRC, DEST, LEN, LEN == MINLEN))
        print("Path from '{}' to '{}': {}".format(SRC, DEST, PATH))
