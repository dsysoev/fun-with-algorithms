
"""
Simple Queue implementation
https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
"""

from __future__ import print_function


class UnderflowQueueError(Exception):
    """ Underflow error implementation """
    def __init__(self):
        super(UnderflowQueueError, self).__init__('the queue is empty')

class OverflowQueueError(Exception):
    """ Overflow error implementation """
    def __init__(self):
        super(OverflowQueueError, self).__init__('the queue is full')

class Queue(object):
    """ simple implementation of Queue

        The Queue a First-In-First-Out (FIFO) data structure.
        In a FIFO data structure, the first element added to the queue
        will be the first one to be removed.

        maxsize : determine maximum items into queue
    """

    def __init__(self, maxsize):
        self.tail = -1
        self.data = []
        self.maxsize = maxsize - 1

    def is_empty(self):
        """ return True if the queue is empty otherwise return False """
        if self.tail == -1:
            return True
        return False

    def is_full(self):
        """ return True if the queue is full otherwise return False """
        if self.tail == self.maxsize:
            return True
        return False

    def enqueue(self, item):
        """ add new item into the queue """
        if self.is_full():
            raise OverflowQueueError()
        self.tail += 1
        self.data.insert(0, item)

    def dequeue(self):
        """ remove last item from the queue """
        if self.is_empty():
            raise UnderflowQueueError()
        self.tail -= 1
        return self.data.pop()

    def peek(self):
        """ show last item in queue """
        if self.is_empty():
            raise UnderflowQueueError()
        return self.data[self.tail]

    def count(self):
        """ number of elements into queu """
        return self.tail + 1

    def __str__(self):
        """ string representation of the queue """
        return str(self.data)

if __name__ in '__main__':
    QUEUE = Queue(maxsize=10)
    for VALUE in range(5):
        print('enqueue {}'.format(VALUE))
        QUEUE.enqueue(VALUE)
    print('show first item: {}'.format(QUEUE.peek()))
    print('show queue: {}'.format(QUEUE))
    print('number of items {}'.format(QUEUE.count()))
    for _ in range(5):
        VALUE = QUEUE.dequeue()
        print('dequeue {}'.format(VALUE))
    print('show queue: {}'.format(QUEUE))
