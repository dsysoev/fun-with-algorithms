

"""
# Structure of a red black tree

1. A node is either red or black.
2. The root is black.
3. All leaves are black.
4. If a node is red, then both its children are black.
5. Every path from a given node to a leaf node has the same
   number of black nodes.
"""

class Node:

    """ Implementaion of red black tree node
        a node has value, color (RED or BLACK),
        parent node (node or None) and left and right child (node or None)
    """

    RED = True
    BLACK = False

    def __init__(self, value, color=RED):
        self.color = color
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.value) + ':' + str('R' if self.color else 'B')

    def verbose(self):
        return '{} (parent:{} left:{} right:{})'.format(
            self, self.parent, self.left, self.right)


class RedBlackTree:

    """ Implementation of Red Black Tree """

    def __init__(self):
        self.root = None

    def max_depth(self, root=None):
        """ return max depth of tree """
        if root is None:
            return 0
        else:
            return max(self.max_depth(root.left),
                       self.max_depth(root.right)) + 1

    def depth(self, node):
        """ returns the value of the node depth
            relative to the root of the tree
        """
        if node is None:
            return 0
        node_ = node
        depth = 0
        while node_ != self.root:
            node_ = node_.parent
            depth += 1
        return depth

    def min(self, current=None):
        """ return minimum value in tree """
        if not current:
            current = self.root
        while current.left is not None:
            current = current.left
        return current

    def max(self, current=None):
        """ return maximum value in tree """
        if not current:
            current = self.root
        while current.right is not None:
            current = current.right
        return current

    def search(self, value):
        """ return a Node with given value otherwise None"""
        return self.__search(self.root, value)

    def __search(self, node, value):
        while node is not None and value != node.value:
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return node

    def successor(self, value):
        """ return a node with nearest number that is more than given """
        current = self.search(value)
        if current is None:
            raise Exception(('a Node with value ({})'
                             ' does not exist').format(value))
        return self.__successor(current)

    def __successor(self, current):

        if current.right is not None:
            return self.min(current.right)
        while (current.parent is not None
               and current.parent.right is current):
            current = current.parent
        return current.parent

    def insert(self, key):
        """ insert a Node with given key to Red Black Tree """
        # define a new Node
        node = Node(key)
        # start from root of tree
        x = self.root
        y = None
        while x is not None:
            # find a parent for Node
            y = x
            if key < x.value:
                x = x.left
            else:
                x = x.right
        # set parent for current Node
        node.parent = y
        if y is None:
            # set Node as new tree root
            self.root = node
        elif key < y.value:
            # set Node as left branch
            y.left = node
        else:
            # set Node as right branch
            y.right = node
        # set default value for current Node
        node.left = None
        node.right = None
        node.color = Node.RED
        # run fixup function for
        # restore red black properties of the tree
        self.__insert_fixup(node)

    def __insert_fixup(self, x):
        """ restore red-black tree properties after insert new node """
        while x != self.root and x.parent.color == Node.RED:
            # we have a violation
            if x.parent == x.parent.parent.left:
                # we are on left branch
                y = x.parent.parent.right
                if y is not None and y.color == Node.RED:
                    # parent is red
                    x.parent.color = Node.BLACK
                    y.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    x = x.parent.parent

                else:
                    # uncle is black
                    if x == x.parent.right:
                        # make x a left child
                        x = x.parent
                        self.__left_rotate(x)
                    # recolor and rotate
                    x.parent.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    self.__right_rotate(x.parent.parent)

            else:
                # mirror image of above code
                y = x.parent.parent.left
                if y is not None and y.color == Node.RED:
                    # parent is red
                    x.parent.color = Node.BLACK
                    y.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    x = x.parent.parent

                else:
                    # parent is black
                    if x == x.parent.left:
                        x = x.parent
                        self.__right_rotate(x)

                    x.parent.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    self.__left_rotate(x.parent.parent)

        self.root.color = Node.BLACK

    def __left_rotate(self, x):
        """ transformation of the left subtree to the right subtree """
        if not x.right:
            raise Exception("a right branch of Node is None")
        # get right subtree
        y = x.right
        # transformation of the left subtree to the right
        x.right = y.left
        if y.left:
            y.left.parent = x
        # set new parent
        y.parent = x.parent
        if not x.parent:
            # set new root
            self.root = y
        else:
            if x == x.parent.left:
                # we are on left branch
                x.parent.left = y
            else:
                x.parent.right = y
        # set x as left parent node
        y.left = x
        x.parent = y

    def __right_rotate(self, x):
        """ transformation of the right subtree to the left subtree """
        if not x.left:
            raise Exception("a right branch of Node is None")
        # get left subtree
        y = x.left
        # transformation of the right subtree to the left
        x.left = y.right
        if y.right:
            y.right.parent = x
        # set new parent
        y.parent = x.parent
        if not x.parent:
            # set new root
            self.root = y
        else:
            if x == x.parent.left:
                # we are on left branch
                x.parent.left = y
            else:
                x.parent.right = y
        # set x as right parent node
        y.right = x
        x.parent = y

    def transplant(self, node, newnode):
        """ transplant new node to current node """
        if node.parent is None:
            self.root = newnode
        elif node == node.parent.left:
            node.parent.left = newnode
        else:
            node.parent.right = newnode
        if newnode is not None:
            newnode.parent = node.parent

    def delete(self, value):
        """ delete value from tree """
        node = self.search(value)
        return self.__delete(node)

    def __delete(self, node):
        y = node
        color = y.color
        if node.left is None:
            x = node.right
            self.transplant(node, node.right)
        elif node.right is None:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.min(node.right)
            color = y.color
            x = y.right
            if x is not None and x.parent is not None and y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y

            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if color == Node.BLACK:
            self.__delete_fixup(x)

    def __delete_fixup(self, x):
        """ restore red-black tree properties after insert new node """
        while x != self.root and x.color == Node.BLACK:
            # we have a violation
            if x == x.parent.left:
                # we are on left branch
                y = x.parent.right
                if y is not None and y.color == Node.RED:
                    # parent is red
                    y.color = Node.BLACK
                    x.parent.color = Node.RED
                    x = x.parent.parent
                    self.__left_rotate(x.parent)
                    y = x.parent.right

                if y.left.color == Node.BLACK and y.right.color == Node.BLACK:
                    y.color = Node.RED
                    x = x.parent
                else:
                    if y.right.color == Node.BLACK:
                        y.left.color = Node.BLACK
                        y.color = Node.RED
                        self.__right_rotate(y)
                        y = x.parent.right
                    y.color = x.parent.color
                    x.parent.color = Node.BLACK
                    y.right.color = Node.BLACK

                    self.__left_rotate(x.parent)
                    x = self.root

            else:

                y = x.parent.left
                if y is not None and y.color == Node.RED:
                    # parent is red
                    y.color = Node.BLACK
                    x.parent.color = Node.RED
                    x = x.parent.parent
                    self.__right_rotate(x.parent)
                    y = x.parent.left

                if y.right.color == Node.BLACK and y.left.color == Node.BLACK:
                    y.color = Node.RED
                    x = x.parent
                else:
                    if y.left.color == Node.BLACK:
                        y.right.color = Node.BLACK
                        y.color = Node.RED
                        self.__left_rotate(y)
                        y = x.parent.left
                    y.color = x.parent.color
                    x.parent.color = Node.BLACK
                    y.left.color = Node.BLACK

                    self.__right_rotate(x.parent)
                    x = self.root

        x.color = Node.BLACK

    def __str__(self):
        """ return a string representation of Tree """
        # a variable to hold the node in ascending order
        sortnodes = []
        # last node in tree
        maxnode = self.max(self.root)
        # first node in tree
        node = self.min(self.root)
        while True:
            sortnodes.append((node, self.depth(node)))
            if node == maxnode:
                break
            # next node
            node = self.__successor(node)
        # max depth of tree
        maxdepth = self.max_depth(self.root)
        # list of tree strings
        strings = ['' for _ in range(maxdepth + 1)]

        for node, rank in sortnodes:
            for level in range(maxdepth + 1):
                if rank == level:
                    strings[level] += str(node)
                else:
                    strings[level] += ' ' * len(str(node))

        return "\n".join(strings)

if __name__ in "__main__":

    tree = RedBlackTree()

    for i in [0, -12, -8, 10, -100]:
        print('insert {} to tree'.format(i))
        tree.insert(i)
    print(tree)

    for i in [-100, -8]:
        tree.delete(i)
        print(tree)
