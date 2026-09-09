# Problem: 242. Valid Anagram
# Difficulty: Easy
# Topics: Hash Table, String, Sorting
# URL: https://leetcode.com/problems/valid-anagram/
# Runtime: 7 ms
# Memory: 17.7 MB
# Solved via CodePath Auto-Committer

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        return a == b
          