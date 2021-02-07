# https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/
# Runtime: 208 ms, faster than 67.60% of Python3 online submissions for Substring with Concatenation of All Words.
# Memory Usage: 13.3 MB, less than 70.00% of Python3 online submissions for Substring with Concatenation of All Words.

from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not words:
            return []

        # check if len shorter than words
        sum_words = sum([len(word) for word in words])
        if len(s) < sum_words:
            return []

        # sort words for correct comparison
        words.sort()

        len_word = len(words[0])
        num_words = len(words)

        outputs = []
        for shift in range(len_word):

            # create all sequence
            seq_words = [s[i:i + len_word] for i in range(shift, len(s), len_word)]

            # create init and queue
            current, queue = seq_words[:num_words - 1], seq_words[num_words - 1:]

            i = -1
            while queue:

                i += 1
                # get from queue
                word = queue.pop(0)
                # add new word
                current.append(word)

                if sorted(current) == words:
                    outputs.append(shift + i * len_word)

                # remove first
                current.pop(0)

        return outputs
