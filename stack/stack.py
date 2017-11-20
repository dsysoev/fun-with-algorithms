
"""
Simple Stack implementation
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
"""

from __future__ import print_function

import re


class UnderflowStackError(Exception):
    """ Underflow error implementation """
    def __init__(self):
        super(UnderflowStackError, self).__init__('the stack is empty')

class OverflowStackError(Exception):
    """ Overflow error implementation """
    def __init__(self):
        super(OverflowStackError, self).__init__('the stack is full')

class Stack(object):
    """ simple implementation of Stack

         The Stack is an abstract data type that serves
         as a collection of elements, with two principal operations:

         - push, which adds an element to the collection
         - pop, which removes the most recently added element
                that was not yet removed.

        The order in which elements come off a stack
        gives rise to its alternative name, LIFO (last in, first out)

        maxsize : determine maximum items into stack
    """

    def __init__(self, maxsize):
        self.head = -1
        self.data = []
        self.maxsize = maxsize - 1

    def is_empty(self):
        """ return True if the Stack is empty otherwise return False """
        if self.head == -1:
            return True
        return False

    def is_full(self):
        """ return True if the Stack is full otherwise return False """
        if self.head == self.maxsize:
            return True
        return False

    def push(self, item):
        """ add new item into Stack """
        if self.is_full():
            raise OverflowStackError()
        self.head += 1
        self.data.append(item)

    def pop(self):
        """ remove last item from Stack """
        if self.is_empty():
            raise UnderflowStackError()
        self.head -= 1
        return self.data.pop()

    def peek(self):
        """ show last item in Stack """
        if self.is_empty():
            raise UnderflowStackError()
        return self.data[self.head]

    def count(self):
        """ number of elements into Stack """
        return self.head + 1

    def __str__(self):
        """ string representation of the stack """
        return str(self.data)

def postfix_calculatior(expression):
    """ Evaluate postfix expressions
        https://en.wikipedia.org/wiki/Reverse_Polish_notation
        E.g. "3 4 + 2 *" = 14
    """
    tokens = re.split("([^0-9])", expression)
    stack = Stack(maxsize=1000)
    for token in tokens:
        token = token.strip()
        if not token:
            continue
        if token == '+':
            result = stack.pop() + stack.pop()
            stack.push(result)
        elif token == '-':
            result = -stack.pop() + stack.pop()
            stack.push(result)
        elif token == '*':
            result = stack.pop() * stack.pop()
            stack.push(result)
        elif token == '/':
            result = 1. / stack.pop() * stack.pop()
            stack.push(result)
        else:
            stack.push(float(token))
    return stack.pop()

if __name__ in '__main__':
    STACK = Stack(maxsize=10)
    for VALUE in range(5):
        print('push {}'.format(VALUE))
        STACK.push(VALUE)
    print('show last item: {}'.format(STACK.peek()))
    print('show stack: {}'.format(STACK))
    print('number of items: {}'.format(STACK.count()))
    for _ in range(5):
        VALUE = STACK.pop()
        print('pop {}'.format(VALUE))
    print('show stack: {}'.format(STACK))
    print('')
    print('Reverse Polish notation calculator:')
    for EXPR in ["4 1 -", "25 5 /", "5 25 /", "3 4 + 2 *",
                 "15 7 1 1 + - / 3 * 2 1 1 + + -"]:
        VALUE = postfix_calculatior(EXPR)
        print('"{}" = {}'.format(EXPR, VALUE))
