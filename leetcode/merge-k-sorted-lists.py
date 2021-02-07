# https://leetcode.com/problems/merge-k-sorted-lists/submissions/
# Runtime: 116 ms, faster than 56.96% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 16.4 MB, less than 56.06% of Python3 online submissions for Merge k Sorted Lists

from typing import List
import sortedcontainers


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        # skip None nodes
        lists = [node for node in lists if node]

        # create sorted queue
        queue = sortedcontainers.SortedList(lists, key=lambda x: x.val)

        # set head node
        head = current = ListNode(0)

        while queue:

            # get lower node
            node = queue.pop(0)

            # swipe next and current
            current.next = node
            current = current.next

            if node.next:
                # add next node
                queue.add(node.next)

        return head.next
