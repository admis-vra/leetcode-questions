# Problem: 242. Valid Anagram
# Difficulty: Easy
# Topics: Hash Table, String, Sorting
# URL: https://leetcode.com/problems/valid-anagram/
# Runtime: 16 ms
# Memory: 18.5 MB
# Solved via CodePath Auto-Committer

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(s)
        b = sorted(t)
        return a == b
          