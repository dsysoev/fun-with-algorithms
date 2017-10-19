

class HashTable(object):
    """ hash table implementation with linked list """

    def __init__(self, size=5):
        """ variable size determines the length of the hash table """
        self.size = size
        self.length = 0
        self.keys = [LinkedList() for _ in range(self.size)]

    def add(self, key, value):
        """ add new key into hash table """
        hash_value = hash_function(key, self.size)
        # get linkedlist for current hash
        linkedlist = self.keys[hash_value]
        # search node with current key
        node = linkedlist.search(key)
        if node is None:
            # add new node
            linkedlist.add(key, value)
            self.length += 1
        else:
            # if node with that key exist
            # change it value
            node.value = value

    def get(self, key, default=None):
        """ get value by key from hash table
            if key does not exist return default value (None)
        """
        hash_value = hash_function(key, self.size)
        # get linkedlist for current hash
        linkedlist = self.keys[hash_value]
        # get node for current hash
        node = linkedlist.search(key)
        return node.value if node is not None else default

    def remove(self, key):
        """ remove key from hash table and return deleted value """
        hash_value = hash_function(key, self.size)
        # get linkedlist for current hash
        linkedlist = self.keys[hash_value]
        node = linkedlist.remove(key)
        if node is None:
            return None
        # if node is exist decrease the counter
        self.length -= 1
        return node.value

    def __len__(self):
        """ number of elements in hash table """
        return self.length

    def __str__(self):
        """ string representation of hash table """
        string = ''
        for item in self.keys:
            node = item.head
            while node is not None:
                string += str(node) + ', '
                node = node.child
        return '{' + string[:-2] + '}'


class Node(object):
    """ a node implementation for linked list """

    def __init__(self, key, value, child=None):
        self.key = key
        self.value = value
        self.child = child

    def __str__(self):
        """ string representation of current node """
        key = self.key
        if isinstance(self.key, str):
            key = "'{}'".format(self.key)
        value = self.value
        if isinstance(self.value, str):
            value = "'{}'".format(self.value)
        return str(key) + ': ' + str(value)

class LinkedList(object):
    """ linked list implementation """

    def __init__(self):
        self.head = None

    def add(self, key, value):
        """ add new element into linked list """
        # create new node
        node = Node(key, value, child=self.head)
        # set head as new node
        self.head = node

    def search(self, key):
        """
        Search linked list and return a Node with given value
        otherwise return None
        """
        current = self.head
        while current is not None:
            if current.key == key:
                return current
            current = current.child
        return None

    def remove(self, key):
        """ delete node from linked list with given value """
        current = self.head
        previous = None
        while current is not None and current.key != key:
            previous = current
            current = current.child

        if previous is None:
            self.head = current.child
        elif current is not None:
            # connect previous Node to next Node
            previous.child = current.child
        return current

    def __str__(self):
        """ string representation of linked list """
        string = ''
        current = self.head
        while current is not None and current.child is not None:
            string += str(current) + ' -> '
            current = current.child
        string += str(current) + ' -> ' + str(None)
        return string

def hash_function(key, size):
    """ simple hash function for certain number of elements """
    return sum([i * 256 + ord(v_) for i, v_ in enumerate(str(key))]) % size

if __name__ in '__main__':
    ht = HashTable()
    DATA = {'hello 0123': 0, '1': '1', 1: 1, 0: -1, 4: 4}

    for k, v in DATA.items():
        ht.add(k, v)
        print('add key', k, 'value', v, 'length', len(ht))

    print('\nhashtable:', ht, '\n')

    print('add key \'hello 0123\'', 'value', -10, 'length', len(ht))
    ht.add('hello 0123', -10)
    print('\nhashtable:', ht, '\n')

    for k in [4, '1', 100]:
        ht.remove(k)
        print('remove key', k, 'length', len(ht))

    print('\nhashtable:', ht, '\n')

    for k in [4, 0, 'hello 0123']:
        print('get value by key', k, 'value:', ht.get(k))
