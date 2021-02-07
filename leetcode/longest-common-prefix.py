# https://leetcode.com/problems/longest-common-prefix/submissions/
# Runtime: 24 ms, faster than 96.99% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def find_longest(word1, word2):
            for i in range(len(word1), 0, -1):
                part = word1[:i]
                if word2.startswith(part):
                    return part

            return ""

        # return "" if empty
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        # for starting with shortest
        sorted_list = sorted(strs, key=len)

        # get shortest element
        prefix = sorted_list.pop(0)

        for word in sorted_list:
            # id not equal
            if prefix != word:
                prefix = find_longest(prefix, word)

        return prefix
