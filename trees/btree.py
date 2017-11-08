

"""
a B-Tree implementation

see more in
[B-tree](https://en.wikipedia.org/wiki/B-tree)

B-tree visualization
[B-Trees](https://www.cs.usfca.edu/~galles/visualization/BTree.html
"""

from __future__ import print_function


class Node(object):
    """ a B-Tree Node implementation

        Parameters
        ----------

        leaf : boolean
               determines whether this node is a leaf.
        keys : list
               a list of keys internal to this node
        childs : list
               a list of children of this node

    """
    def __init__(self, leaf):
        self.leaf = leaf
        self.keys = []
        self.childs = []

    def __str__(self):
        return str(self.keys)

class Tree(object):
    """ a B-Tree implementation """

    def __init__(self, t):
        self.root = Node(leaf=True)
        self.t = t

    def search(self, key):
        """ Search the key in the B-Tree

            Parameters
            ----------
            key : int
                  the key for search

            Returns
            -------
            out : tuple(Node, int)
                  if key does not exist in the tree a Node equal to None

        """
        return self._search(key, self.root)

    def _search(self, key, node):
        """ recursive function for search the key """
        i = 0
        # looking for an index for given key
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            # index found
            return node, i
        elif node.leaf:
            # no match if node is a leaf
            return None, None
        else:
            # search key in children
            return self._search(key, node.childs[i])

    def insert(self, key):
        """ Insert the key in B-Tree

            Parameters
            ----------
            key : int
                  the key for insert

            Returns
            -------
            out : None

        >>> TREE = Tree(t=2); a = [TREE.insert(i) for i in range(10)]; TREE.root.keys
        [3]
        """
        # start from root of the tree
        # parent is None
        self._insert(node=self.root, parent=None, key=key)

    def _insert(self, node, parent, key):
        """ recursive function for insert the key into B-Tree """
        i = 0
        if node.leaf:
            # if the node is a leaf
            # find position and
            # insert a key
            for i in range(len(node.keys) - 1, -1, -1):
                if key > node.keys[i]:
                    i += 1
                    break
            node.keys.insert(i, key)
        else:
            # call recursive function for child node
            for i in range(len(node.keys) - 1, -1, -1):
                if key > node.keys[i]:
                    i += 1
                    break
            self._insert(node.childs[i], node, key)

        self._check_and_split(node, parent)

    def _check_and_split(self, node, parent):
        """ function checks if a split is required and does it if necessary """
        if len(node.keys) == 2 * self.t:
            # number of keys equal maximum value
            # start _split_child function
            if parent is None:
                # create new root Node
                newnode = Node(leaf=False)
                self.root = newnode
                newnode.childs.insert(0, node)
                self._split_child(newnode, 0)
            else:
                # split children in parent node
                i = 0
                for i, item in enumerate(parent.childs):
                    if item.keys == node.keys:
                        break
                self._split_child(parent, i)

    def _split_child(self, node, i):
        """ the method splits the child node into two nodes """
        # get child node (left after split)
        y = node.childs[i]
        # set new node (right after split)
        z = Node(leaf=y.leaf)
        # get t value
        t = self.t
        # save key
        key = y.keys[t - 1]
        # move keys to right node
        z.keys = y.keys[t:2 * t]
        # store keys for left node
        y.keys = y.keys[0:t - 1]
        if not y.leaf:
            # move children to right node
            z.childs = y.childs[t:2 * t + 1]
            # and for left node
            y.childs = y.childs[0:t]
        # insert key to parent node
        node.keys.insert(i, key)
        # add new node to parent node
        node.childs.insert(i + 1, z)

    def __str__(self):
        """ Print a tree an level-order representation. """
        strlist = []
        thislevel = [self.root]
        while thislevel:
            nextlevel = []
            output = ""
            for node in thislevel:
                if not node.leaf:
                    nextlevel.extend(node.childs)
                output += str(node) + " "
            strlist.append(output)
            thislevel = nextlevel
        # get length of the biggest level of tree
        length = len(strlist[-1])
        # move levels to the center of string
        lst = [s.center(length) for s in strlist]
        return "\n".join(lst)

if __name__ in '__main__':
    TREE = Tree(t=2)
    for VALUE in [8, 13, 5, 0, 16, 7, 23, 15, 1, 2, 3]:
        print('insert {}'.format(VALUE))
        TREE.insert(VALUE)
        print('TREE:')
        print(TREE, '\n')

    for VALUE in [8, 10, 23, 3]:
        NODE, ITEM = TREE.search(VALUE)
        print('search {}: {} {}'.format(VALUE, NODE, ITEM))
