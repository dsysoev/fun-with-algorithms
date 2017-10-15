
class Node:
    """ a node representation for binary search tree """
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.value)

    def verbose(self):
        return '{} (parent:{} left:{} right:{})'.format(
            self.value, self.parent, self.left, self.right)

class Tree:
    """ Binary search tree implementation"""
    def __init__(self):
        self.root = None

    def add(self, value):
        """ add new element into binary tree return new Node """
        if self.root is None:
            self.root = Node(value, parent=self.root)
            return self.root
        else:
            return self._add(self.root, value)

    def _add(self, node, value):
        # skip duplicated elements
        if value == node.value:
            return None
        # going to left branch
        elif value < node.value:
            if node.left is not None:
                return self._add(node.left, value)
            else:
                # add new Node if child is empty
                node.left = Node(value, parent=node)
                return node.left
        # going to right branch
        else:
            # add new Node if child is empty
            if node.right is None:
                node.right = Node(value, parent=node)
                return node.right
            else:
                return self._add(node.right, value)

    def search(self, value, node=None):
        """ return a Node with given value otherwise None"""
        if node is None:
            node = self.root
        return self._search_iterative(node, value)

    def _search_iterative(self, node, value):
        while node is not None and value != node.value:
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return node

    def rank(self, value):
        """ return rank in tree for given value """
        return self._rank(self.root, value)

    def _rank(self, node, value):
        if node is None:
            return 0
        elif value == node.value:
            return 1 + self._rank(node.left, value)
        elif value > node.value:
            return 1 + self._rank(node.left, value) \
                                    + self._rank(node.right, value)
        elif value < node.value:
            return self._rank(node.left, value)
        else:
            return 0

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

    def successor(self, value):
        """ return a Node with nearest number that is more than given """
        current = self.search(value)
        if current is None:
            raise Exception(('a Node with value ({})'
                             ' does not exist').format(value))
        return self._successor(current)

    def _successor(self, current):

        if current.right is not None:
            return self.min(current.right)
        while (current.parent is not None
               and current.parent.right is current):
            current = current.parent
        return current.parent

    def preccessor(self, value):
        """ return a Node with nearest number that is less than given """
        current = self.search(value)
        if current is None:
            raise Exception(('a Node with value ({})'
                             ' does not exist').format(value))
        return self._precessor(current)

    def _precessor(self, current):

        if current.left is not None:
            return self.max(current.left)
        while current.parent is not None and current.parent.left is current:
            current = current.parent
        return current.parent

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
        """ Delete a Node with given value """
        node = self.search(value, self.root)
        if node is None:
            raise Exception(('a Node with value ({})'
                             ' does not exist').format(value))

        return self._delete(node)

    def _delete(self, node):

        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            successor = self.min(node.right)
            if successor.parent != node:
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def max_depth(self, root=None):
        if root is None:
            return 0
        else:
            return max(self.max_depth(root.left),
                       self.max_depth(root.right)) + 1

    def depth(self, node):
        if node is None:
            return 0
        node_ = node
        depth = 0
        while node_ != self.root:
            node_ = node_.parent
            depth += 1
        return depth

    def __str__(self):
        node = self.min(self.root)

        sortnodes = []
        maxnode = self.max(self.root)
        maxdepth = self.max_depth(self.root)

        while True:
            sortnodes.append((node, self.depth(node)))
            if node == maxnode:
                break
            node = self._successor(node)

        strings = ['' for _ in range(maxdepth + 1)]

        for node, rank in sortnodes:
            for level in range(maxdepth + 1):
                if rank == level:
                    strings[level] += str(node)
                else:
                    strings[level] += ' ' * len(str(node))

        return "\n".join(strings)


if __name__ in "__main__":

    print('create empty tree')
    tree = Tree()
    treeNodes = {}
    for i in [10, -2, 20, 100, 101,
              2, 3, 4, 5, 6, 90,
              80, -10, -20, 15]:
        print('add {}'.format(i))
        treeNodes[i] = tree.add(i)

    print('initial tree:\n', tree, '\n')

    tree2 = Tree()
    tree2Nodes = {}
    for i in [0, 1, 7, 14, 11, -1]:
        tree2Nodes[i] = tree2.add(i)
    print()

    print('another tree:\n', tree2, '\n')

    print('transplant element 1 from another tree to element 3 of initial tree')
    tree.transplant(treeNodes[3], tree2Nodes[1])

    print(tree)
    print()

    for i in [2, 20, 10]:
        print('delete element {} from tree'.format(i))
        tree.delete(i)

        print(tree)
        print()

    for i in [-6, 90, 100]:
        print('search value {}:'.format(i), tree.search(i))
    print()

    for i in [15, 100, -2]:
        print('successor value {}:'.format(i), tree.successor(i))
    print()

    for i in [-10, 15, -2]:
        print('preccessor value {}:'.format(i), tree.preccessor(i))
    print()

    print('min value:', tree.min())
    print('max value:', tree.max())
