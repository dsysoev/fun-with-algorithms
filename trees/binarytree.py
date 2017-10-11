
class Node:
    """ a node representation for binary search tree """
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def __str__(self):
        return str(self.value) + ' (' + str(self.parent) + ')'

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
            if node.leftChild:
                return self._add(node.leftChild, value)
            else:
                # add new Node if child is empty
                node.leftChild = Node(value, parent=node)
                return node.leftChild
        # going to right branch
        else:
            if node.rightChild:
                return self._add(node.rightChild, value)
            else:
                # add new Node if child is empty
                node.rightChild = Node(value, parent=node)
                return node.rightChild

    def search(self, value, node=None):
        """ return a Node with given value otherwise None"""
        if node is None:
            node = self.root
        return self._search_iterative(node, value)

    def _search_recursive(self, node, value):
        if node is None or value == node.value:
            return node
        elif value < node.value:
            return self._search(node.leftChild, value)
        else:
            return self._search(node.rightChild, value)

    def _search_iterative(self, node, value):
        while node is not None and value != node.value:
            if value < node.value:
                node = node.leftChild
            else:
                node = node.rightChild
        return node

    def rank(self, value):
        """ return rank in tree for given value """
        return self._rank(self.root, value)

    def _rank(self, node, value):
        if node is None:
            return 0
        if value == node.root:
            return 1 + self._rank(node.leftChild, value)
        elif value > node.root:
            return 1 + self._rank(node.leftChild, value) \
                                    + self._rank(node.rightChild, value)
        elif value < node.root:
            return self._rank(node.leftChild, value)
        else:
            return 0

    def min(self, current=None):
        """ return minimum value in tree """
        if not current:
            current = self.root
        while current.leftChild is not None:
            current = current.leftChild
        return current

    def max(self, current=None):
        """ return maximum value in tree """
        if not current:
            current = self.root
        while current.rightChild is not None:
            current = current.rightChild
        return current

    def successor(self, value):
        """ return a Node with nearest number that is more than given """
        current = self.search(value)
        if current is None:
            return None

        if current.rightChild is not None:
            return self.min(current.rightChild)
        while current.parent is not None \
                and current.parent.rightChild is current:
            current = current.parent
        return current.parent

    def preccessor(self, value):
        """ return a Node with nearest number that is less than given """
        current = self.search(value)
        if current is None:
            return None

        if current.leftChild is not None:
            return self.max(current.leftChild)
        while current.parent is not None and current.parent.leftChild is current:
            current = current.parent
        return current.parent

    def transplant(self, node, newnode):
        """ transplant NewNode to current Node """
        if node.parent is None:
            self.root = newnode
        elif node == node.parent.leftChild:
            node.parent.leftChild = newnode
        else:
            node.parent.rightChild = newnode
        if newnode is not None:
            newnode.parent = node.parent

    def delete(self, value, current=None):
        """ Delete a Node with given value """
        if current is None:
            current = self.root
        node = self.search(value, current)

        if node.leftChild is None:
            self.transplant(node, node.rightChild)
        elif node.rightChild is None:
            self.transplant(node, node.leftChild)
        else:
            successor = self.min(node.rightChild)
            if successor.parent != node:
                self.transplant(successor, successor.rightChild)
                successor.rightChild = node.rightChild
                successor.rightChild.parent = successor
            self.transplant(node, successor)
            successor.leftChild = node.leftChild
            successor.leftChild.parent = successor

    def __str__(self):
        """ string presentation of Binary Search Tree """
        def _str(node):
            if node is None:
                return [], 0, 0
            label = str(node.value)
            # get lines, position and wigth for left and right child
            leftLines, leftPos, leftWidth = _str(node.leftChild)
            rightLines, rightPos, rightWidth = _str(node.rightChild)
            # determine middle position
            middle = max(rightPos + leftWidth - leftPos + 1, len(label), 2)
            pos = leftPos + middle // 2
            width = leftPos + middle + rightWidth - rightPos
            # append spaces for left lines
            while len(leftLines) < len(rightLines):
                leftLines.append(' ' * leftWidth)
            # append spaces for right lines
            while len(rightLines) < len(leftLines):
                rightLines.append(' ' * rightWidth)
            # put label into center of string and add dots
            label = label.center(middle, '_')
            # create string
            lines = [' ' * leftPos + label + ' ' * (rightWidth - rightPos),
                     ' ' * leftPos + '/' + ' ' * (middle - 2) +
                     '\\' + ' ' * (rightWidth - rightPos)]
            spaceLine = ' ' * (width - leftWidth - rightWidth)
            lines += [leftLine + spaceLine + rightLine
                        for leftLine, rightLine in zip(leftLines, rightLines)]

            return lines, pos, width

        if self.root is None: return '<empty tree>'
        return '\n'.join(_str(self.root) [0])

if __name__ in "__main__":

    print('create empty tree')
    tree = Tree()
    d = {}
    for i in [10, 10, 0, 20, -10, 100]:
        print('add {}'.format(i))
        d[i] = tree.add(i)

    print('initial tree:\n', tree, '\n')

    for i in [3]:
        print('add {}'.format(i))
        d[i] = tree.add(i)

    print('initial tree:\n', tree, '\n')

    tree2 = Tree()
    d2 = {}
    for i in [1, 7, 4 -1]:
        d2[i] = tree2.add(i)
    print()

    print('another tree:\n', tree2, '\n')

    print('transplant element 1 from another tree to element 3 of initial tree')
    tree.transplant(d[3], d2[1])

    print(tree)
    print()

    for i in [3, 0, 10]:
        print('delete element {} from tree'.format(i))
        tree.delete(i)

        print(tree)
        print()

    for i in [-6, 20, 100]:
        print('search value {}:'.format(i), tree.search(i))
    print()

    for i in [20, 100, 0]:
        print('successor value {}:'.format(i), tree.successor(i))
    print()

    for i in [-10, 10, 0]:
        print('preccessor value {}:'.format(i), tree.preccessor(i))
    print()

    print('min value:', tree.min())
    print('max value:', tree.max())
