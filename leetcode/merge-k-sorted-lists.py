# https://leetcode.com/problems/merge-k-sorted-lists/submissions/
# Runtime: 128 ms, faster than 42.22% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Merge k Sorted Lists.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        # remove None nodes
        lists = [node for node in lists if node]

        # get lower node
        lists.sort(key=lambda x: x.val)

        merged = None
        while lists:

            # get lower value
            node = lists.pop(0)

            # for first iteration only
            if merged is None:
                merged = node
                merged_node = merged
            else:
                merged_node.next = node
                merged_node = merged_node.next

            if node.next is not None:
                # add to next iteration
                lists.append(node.next)
                lists.sort(key=lambda x: x.val)

        return merged
