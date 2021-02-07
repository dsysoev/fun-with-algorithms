

from __future__ import print_function


class Node(object):
    """ a node representation in linked list """

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        """ return node data """
        return str(self.data)

    def get_next(self, isnext):
        """ return next element if isnext=True, otherwise return previous """
        return self.next if isnext else self.prev

    def get_prev(self, isnext):
        """ return previous element if isnext=True, otherwise return next """
        return self.get_next(not isnext)

    def add_next(self, isnext, node):
        """ add node to self.next if isnext=True
            otherwise add it to self.prev
        """
        if isnext:
            self.next = node
        else:
            self.prev = node

    def add_prev(self, isnext, node):
        """ add a node to self.prev if isnext=True
            otherwise add it to self.next
        """
        self.add_next(not isnext, node)

    def verbose(self):
        """ return node presentation """
        return ('prev:' + str(self.prev) +
                ' data:' + str(self.data) +
                ' next:' + str(self.next))


class Nil(Node):
    """ Nil node implementation """

    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None
        super().__init__(data=self.data, next=self.next, prev=self.prev)


class LinkedList(object):
    """ simple linked list representation """

    def __init__(self):
        self.head = Nil()
        self.tail = Nil()
        # if isnext = True move in a direct pass
        # otherwise move in inverse pass
        self.isnext = True

    def add(self, data):
        """ add new element into linked list """
        # create new node
        node = Node(data)
        # add next element
        node.add_next(self.isnext, self.head)
        if self.head.data is None:
            # save tail node
            self.tail = node
        else:
            # add previous element to head
            self.head.add_prev(self.isnext, node)
        # set head as new node
        self.head = node

    def reversed(self):
        """ reversed linked list for O(1) """
        # swap head and tail
        self.head, self.tail = self.tail, self.head
        # change direct pass to inverse
        self.isnext = not self.isnext
        # add Nil node to tail
        self.tail.add_next(self.isnext, Nil())

    def search(self, value):
        """
            search linked list and return a Node with given value
            otherwise return None
        """
        current = self.head
        while current.data is not None:
            if current.data == value:
                return current
            current = current.get_next(self.isnext)
        return None

    def remove(self, value):
        """ delete a node from linked list with given value """
        current = self.head
        while current.data is not None and current.data != value:
            current = current.get_next(self.isnext)

        if current.data is not None:
            # connect previous Node to next Node
            next_ = current.get_next(self.isnext)
            previous = current.get_prev(self.isnext)
            previous.add_next(self.isnext, next_)
            next_.add_prev(self.isnext, previous)

    def __str__(self):
        """ presented linked list objects as string
            node.data -> NextNode.data
        """
        string = ''
        current = self.head
        while current.get_next(self.isnext) is not None:
            string += str(current.data) + ' -> '
            current = current.get_next(self.isnext)
        string += str(current.data)
        return string


if __name__ in "__main__":
    print('create initial linked list')
    LIST = LinkedList()
    for i in [1, -10, 3]:
        print('add {}'.format(i))
        LIST.add(i)
    print()

    print('linked list:', LIST, '\n')

    LIST.reversed()
    print('list reversed\n')
    print('linked list:', LIST, '\n')

    LIST.reversed()
    print('list reversed\n')
    print('linked list:', LIST, '\n')

    for i in [3, 10]:
        print('search {}'.format(i), LIST.search(i))
    print('')

    for i in [1, 4, -10]:
        LIST.remove(i)
        print('remove {}'.format(i))
        print('linked list:', LIST, '\n')
