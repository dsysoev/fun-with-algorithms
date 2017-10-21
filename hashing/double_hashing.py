

class HashTable(object):
    """ hash table implementation with double hashing and open addressing """

    def __init__(self, size):
        """ size - determines the maximum length of the hash table
            length - number of elements in hash table
            keys - variable to store nodes
        """
        self.size = size
        self.length = 0
        self.keys = [None for _ in range(self.size)]

    def add(self, key, value):
        """ add new key, value into hash table """
        # working to max size of table
        for i in range(self.size):
            # get hash
            hash_value = hash_function(key, i, self.size)
            # get node or None
            node = self.keys[hash_value]

            if node is None:
                # create new Node
                self.keys[hash_value] = Node(key, value)
                self.length += 1
                return self.keys[hash_value]
            elif node.key == key:
                # update value in node
                self.keys[hash_value].value = value
                if self.keys[hash_value].deleted:
                    self.length += 1
                # restore deleted node
                self.keys[hash_value].deleted = False
                return self.keys[hash_value]

        raise Exception('The hash table is full')

    def get(self, key, default=None):
        """ get value by key from hash table
            if key does not exist in table return default value (None)
        """
        # working to max size of table
        for i in range(self.size):
            # get hash
            hash_value = hash_function(key, i, self.size)
            # get node
            node = self.keys[hash_value]
            if node is None:
                return default
            # if node deleted going to next iteration
            elif not node.deleted and node.key == key:
                return node.value
        return default

    def remove(self, key):
        """ remove key from hash table and return deleted value
            or None if key does not exist in hash table
        """
        # working to max size of table
        for i in range(self.size):
            # get hash
            hash_value = hash_function(key, i, self.size)
            # get node
            node = self.keys[hash_value]
            if node is None:
                return None
            elif node.key == key and not node.deleted:
                # set flag deleted
                node.deleted = True
                # decrease the counter
                self.length -= 1
                return node.value
        return None

    def __len__(self):
        """ number of elements in hash table """
        return self.length

    def __str__(self):
        """ string representation of hash table """
        string = ''
        for item in self.keys:
            if item is None:
                continue
            if item.deleted:
                continue
            string += str(item) + ', '
        return '{' + string[:-2] + '}'


class Node(object):
    """ simple node representation for hash table """

    def __init__(self, key, value):
        """ deleted - this flag used for deleted keys """
        self.key = key
        self.value = value
        self.deleted = False

    def __str__(self):
        """ string representation of current node """
        key = self.key
        if isinstance(self.key, str):
            key = "'{}'".format(self.key)
        value = self.value
        if isinstance(self.value, str):
            value = "'{}'".format(self.value)
        return str(key) + ': ' + str(value)

def hash_function(key, item, size):
    """ hash function = (h1(key) + item * h2(key)) % size """
    hash_value = hash_1(key, size)
    if item == 0:
        return hash_value

    return (hash_value + item * hash_2(key, size - 1)) % size

def hash_1(key, size):
    """ simple hash 1 function """
    return sum([i * 256 + ord(v_) for i, v_ in enumerate(str(key))]) % size

def hash_2(key, size):
    """ simple hash 2 function """
    return sum([i * 256 + ord(v_) + i for i, v_ in enumerate(str(key))]) % size

if __name__ in '__main__':
    ht = HashTable(size=100)
    DATA = {'hello 0123': 0, '1': '1', 1: 1, 0: -1, 4: 4}
    for k, v in DATA.items():
        ht.add(k, v)
        print('add key', k, 'value', v, 'length', len(ht))
    print('\nhashtable:', ht, '\n')

    print('add key \'hello 0123\'', 'value', -10, 'length', len(ht))
    ht.add('hello 0123', -10)
    print('\nhashtable:', ht, '\n')

    for k in [4, '1', 100, 4]:
        ht.remove(k)
        print('remove key', k, 'length', len(ht))
    print('\nhashtable:', ht, '\n')

    for k in [4]:
        ht.add(k, k)
        print('add key', k, 'value', k, 'length', len(ht))
    print('\nhashtable:', ht, '\n')

    for k in [4, 0, 'hello 0123']:
        print('get value by key', k, 'value:', ht.get(k))
