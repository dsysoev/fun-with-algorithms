
"""
Implementation of Floyd Warshall algorithm
https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
"""

from __future__ import print_function


def adjacency_matrix(edges):
    """
    Convert a directed graph to an adjacency matrix.

    Note: The distance from a node to itself is 0 and distance from a node to
    an unconnected node is defined to be infinite.

    Parameters
    ----------
    edges : list of tuples
            list of dependencies between nodes in the graph
            [(source node, destination node, weight), ...]

    Returns
    -------
    out : tuple
          (names, adjacency matrix)
          names - list of unique nodes in the graph
          adjacency matrix represented as list of lists

    """
    # determine the set of unique nodes
    names = set()
    for src, dest, _ in edges:
        # add source and destination nodes
        names.add(src)
        names.add(dest)
    # convert set of names to sorted list
    names = sorted(names)
    # determine initial adjacency matrix with infinity weights
    matrix = [[float('Inf')] * len(names) for _ in names]
    for src, dest, weight in edges:
        # update weight in adjacency matrix
        matrix[names.index(src)][names.index(dest)] = weight

    for src in names:
        matrix[names.index(src)][names.index(src)] = 0
    # return list of names and adjacency matrix
    return names, matrix

def floyd_warshall(edges):
    """
    Floyd-Warshall algorithm implementation

    Find the cost of the shortest path between every pair of vertices in a
    weighted graph.

    Parameters
    ----------
    edges : list of tuples
            list of dependencies between nodes in the graph
            [(source node, destination node, weight), ...]

    Returns
    -------
    out : tuple
          (names, distance matrix, precedence matrix)
          names - list of unique nodes in the graph
          adjacency matrix represented as list of lists
          precedence matrix represented as list of lists

    """
    # get unique node names and adjacency matrix
    names, distance = adjacency_matrix(edges)
    num = len(names)
    # determine initial precedence matrix
    precedence = [[0] * num for _ in range(num)]
    for i in range(num):
        # set infinity value
        precedence[i][i] = float('Inf')
    for src, dest, _ in edges:
        # update precedence
        precedence[names.index(src)][names.index(dest)] = names.index(dest)

    for k in range(num):
        # k is a intermediate node
        for src in range(num):
            # source node
            for dest in range(num):
                # destination node
                intermediate = distance[src][k] + distance[k][dest]
                if intermediate < distance[src][dest]:
                    # for case
                    # then distance from intermediate node
                    # lower than direct path
                    distance[src][dest] = intermediate
                    precedence[src][dest] = precedence[src][k]
    return names, distance, precedence

def print_matrix(matrix, names=None):
    """ simple print funtion for matrix

    Parameters
    ----------
    matrix : list of lists
             matrix represented in list of lists
    names : optional, list
            list of matrix columns and rows names

    Returns
    -------
    out : None

    """
    if names is None:
        names = range(len(matrix))
    # print header
    print('  ', *names)
    for name, item in zip(names, matrix):
        # print line
        print(name, item)

if __name__ == "__main__":
    EDGES = [
        ('s', 't', 6),
        ('s', 'y', 7),
        ('t', 'x', 5),
        ('x', 't', 20),
        ('t', 'y', 8),
        ('y', 'z', 9),
        ('y', 'x', 30),
        ('t', 'z', 40),
        ('z', 's', 2),
        ('z', 'x', 7)
    ]
    print('Show a graph in adjacency list: ')
    for SRC, DEST, WEIGHT in EDGES:
        print("{} -> {} ({})".format(SRC, DEST, WEIGHT))
    NAMES, ADJ_MATRIX = adjacency_matrix(EDGES)
    print('Convert the graph to adjacency matrix:')
    print_matrix(ADJ_MATRIX, NAMES)
    NAMES, DIST, _ = floyd_warshall(EDGES)
    print('Show matrix of shortest distances between nodes')
    print_matrix(DIST, NAMES)
