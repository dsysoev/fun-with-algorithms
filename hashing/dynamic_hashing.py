

from __future__ import print_function

import math

class HashTable(object):
    """ dynamic hash table implementation with open addressing """

    # deleted flag
    DELETED = True

    def __init__(self, capacity=1):
        """ length - number of elements in hash table
            keys - variable to store nodes
        """
        self.capacity = capacity
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.length = 0

    def add(self, key, value):
        """ the method increases the capacity by 2 times if necessary and
            add new (key, value) into hash table
        """
        if self.length == self.capacity:
            # the hash table if full
            # increase capacity by 2 times
            capacity = self.capacity * 2
            self._change_capacity(capacity)
        # add key and value
        self._add(key, value)

    def _add(self, key, value):
        """ add key and value into hash table """
        for i in range(self.capacity):
            # get hash
            hash_value = hash_function(key, i, self.capacity)
            element = self.keys[hash_value]
            if element is None:
                # add new element
                self.keys[hash_value] = key
                self.values[hash_value] = value
                self.length += 1
                return self.values[hash_value]
            elif element is self.DELETED:
                # find next element
                pass
            elif element == key:
                # update value for current key
                self.values[hash_value] = value
                return self.values[hash_value]

        raise Exception('The hash table is full')

    def _change_capacity(self, capacity):
        """ method change the capacity of hash table """
        # create new hash table
        newtable = HashTable(capacity)
        for i, key in enumerate(self.keys):
            if key is None or key is self.DELETED:
                continue
            # add elements
            newtable._add(key, self.values[i])
        # replacing current table to new table
        self.capacity = newtable.capacity
        self.length = newtable.length
        self.keys = newtable.keys
        self.values = newtable.values

    def get(self, key, default=None):
        """ get value by key from hash table
            if key does not exist in table return default value (None)
        """
        # working to capacity
        for i in range(self.capacity):
            hash_value = hash_function(key, i, self.capacity)
            element = self.keys[hash_value]
            if element is None:
                return default
            elif element is self.DELETED:
                # element is deleted
                # going to next iteration
                pass
            elif element == key:
                return self.values[hash_value]
        return default

    def remove(self, key):
        """ remove key from hash table and return deleted value
            or None if key does not exist in hash table
            change capacity of hash table if count of elements
            in hash table less than or equal to one fourth
        """
        if self.length // self.capacity <= 1 / 4:
            # decrease capacity to next power of two elements
            if self.length == 0:
                capacity = 1
            else:
                capacity = 2 ** math.ceil(math.log(self.length, 2))
            self._change_capacity(capacity)
        # remove key
        return self._remove(key)

    def _remove(self, key):
        """ remove element with current key """
        for i in range(self.capacity):
            hash_value = hash_function(key, i, self.capacity)
            element = self.keys[hash_value]
            if element is None:
                return None
            elif element is self.DELETED:
                # going to next
                pass
            elif element == key:
                # set flag deleted
                self.keys[hash_value] = self.DELETED
                self.length -= 1
                return self.values[hash_value]
        return None

    def __len__(self):
        """ number of elements in hash table """
        return self.length

    def __str__(self):
        """ string representation of hash table """
        string = ''
        for i, key in enumerate(self.keys):
            if key is None:
                continue
            if key is self.DELETED:
                continue
            string += str(key) + ': ' + str(self.values[i]) + ', '
        return '{' + string[:-2] + '}'

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
    TABLE = HashTable()
    # add new elements into table
    for k in range(10):
        print('add key', k, 'value', k * 10)
        TABLE.add(k, k * 10)
    print('\nhashtable:', TABLE, '\n')
    print('keys', TABLE.keys)
    print('values', TABLE.values, '\n')
    # remove elements into table
    for k in range(10):
        print('remove key', k)
        TABLE.remove(k)
    print('\nhashtable:', TABLE, '\n')
    print('keys', TABLE.keys)
    print('values', TABLE.values, '\n')
