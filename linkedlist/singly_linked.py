
class Node:
    """a node representation in linked list"""

    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    def __str__(self):
        """return node data"""
        return str(self.data)

class LinkedList:
    """simple linked list representation"""

    def __init__(self):
        self.head = None

    def add(self, data):
        """ add new element into linked list """
        # create new node
        node = Node(data, self.head)
        # set head as new node
        self.head = node

    def search(self, value):
        """
        Search linked list and return a Node with given value
        otherwise return None
        """
        current = self.head
        while current is not None:
            if current.data == value:
                return current
            current = current.next
        return None

    def remove(self, value):
        """ Delete Node from linked list with given value """
        current = self.head
        previous = None
        while current is not None and current.data != value:
            previous = current
            current = current.next

        if previous is None:
            self.head = current.next
        elif current is not None:
            # connect previous Node to next Node
            previous.next = current.next

    def __str__(self):
        """ Presented linked list objects as string
        Node.data -> NextNode.data
        """
        string = ''
        current = self.head
        while current.next is not None:
            string += str(current.data) + ' -> '
            current = current.next
        string += str(current.data) + ' -> ' + str(None)
        return string

if __name__ in "__main__":

    print('create initial linked list')
    lst = LinkedList()

    for i in [1, 7, 2, 3, -10]:
        print('add {}'.format(i))
        lst.add(i)
    print()

    print('linked list:', lst, '\n')
    for i in [2, 4, -10]:
        lst.remove(i)
        print('remove {}'.format(i))
        print('linked list:', lst, '\n')

    for i in [3, 10]:
        print('search {}'.format(i), lst.search(i))
