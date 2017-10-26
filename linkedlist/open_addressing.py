

from __future__ import print_function

class LinkedList(object):
    """ linked list implementation with open addressing """

    def __init__(self, size):
        """ size - determines the maximum length of the linked list
            keys - variable to store key value
            free - variable to store free items in keys
        """
        self.size = size
        # zero element always None
        self.head = 0
        # set keys list with following structure
        # [key0, next0, previous0, key1, ...]
        self.keys = [None for _ in range(self.size * 3)]
        self.free = list(reversed(range(1, self.size)))

    def add(self, key):
        """ add new key, value into hash table """
        if not self.free:
            # linked list is full
            raise Exception('The linked list is full')
        # get last free key
        position = self.free.pop()
        # set key into keys
        self.keys[position * 3] = key
        # set next item as current head
        self.keys[position * 3 + 1] = self.head
        # set next for previous element
        self.keys[(position - 1) * 3 + 2] = position * 3
        # update head
        self.head = position * 3

    def search(self, key, default=None):
        """ get value by key from linked list
            if key does not exist in table return default value (None)
        """
        i = self.head
        val = self.keys[i]
        while val is not None and val != key:
            # find key in linked list
            i = self.keys[i + 1]
            val = self.keys[i]
        return val if val else default

    def remove(self, key):
        """ remove key from linked list and return deleted value
            or None if key does not exist
        """
        i = self.head
        val = self.keys[i]
        # find item with given key
        while val is not None and val != key:
            i = self.keys[i + 1]
            val = self.keys[i]
        # return None if key not in linked list
        if val is None:
            return None
        # add new empty cell
        self.free.append(i // 3)
        if self.head == i:
            # delete current head
            self.head = self.keys[i + 1]
            self.keys[self.head + 1] = None
            self.keys[self.head + 2] = None
        else:
            # delete element
            self.keys[i] = None
            next_ = self.keys[i + 1]
            prev = self.keys[i + 2]
            self.keys[prev + 1] = next_
            self.keys[next_ + 2] = prev
        # set None for current element
        self.keys[i] = None
        self.keys[i + 1] = None
        self.keys[i + 2] = None
        return val

    def __str__(self):
        """ string representation of linked list """
        i = self.head
        val = self.keys[i]
        string = ''
        while val is not None:
            # add key to string
            string += str(val) + ' -> '
            # update item
            i = self.keys[i + 1]
            val = self.keys[i]
        return '{' + string + 'None}'

if __name__ in '__main__':
    # create empty linked list
    LINKED_LIST = LinkedList(size=5)
    # add keys
    for k in [10, 20]:
        LINKED_LIST.add(k)
        print('add {}'.format(k))
    print('linked list: ', LINKED_LIST)
    # get key
    for k in [10, 20, 30]:
        print('search key {}:'.format(k), LINKED_LIST.search(k))
    # remove key
    for k in [10, 30]:
        LINKED_LIST.remove(k)
        print('remove {}'.format(k))
    print('linked list: ', LINKED_LIST)
    # add key
    for k in [10, 0, -10]:
        LINKED_LIST.add(k)
        print('add {}'.format(k))
    print('linked list: ', LINKED_LIST)
