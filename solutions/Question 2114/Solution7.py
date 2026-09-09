# Problem: 2114. Maximum Number of Words Found in Sentences
# Difficulty: Easy
# Topics: Array, String
# URL: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
# Runtime: 4 ms
# Memory: 17.9 MB
# Solved via CodePath Auto-Committer

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        a = 0
        for b in sentences:
            x = b.split(" ")
            a = max(a,len(x))
        return a