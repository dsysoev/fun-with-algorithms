# https://leetcode.com/problems/longest-common-prefix/submissions/
# Runtime: 24 ms, faster than 96.99% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.

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

        # get len of words
        tuples_list = ((len(word), i) for i, word in enumerate(strs))

        # sorted it, for starting with shortest
        sorted_list = sorted(tuples_list)

        # get first element
        _, i = sorted_list.pop(0)
        prefix = strs[i]

        for len_word, i in sorted_list:
            # equal
            if prefix == strs[i]:
                continue

            else:
                prefix = find_longest(prefix, strs[i])

        return prefix
