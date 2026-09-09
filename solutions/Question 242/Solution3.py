# Problem: 242. Valid Anagram
# Difficulty: Easy
# Topics: Hash Table, String, Sorting
# URL: https://leetcode.com/problems/valid-anagram/
# Runtime: 15 ms
# Memory: 18.6 MB
# Solved via CodePath Auto-Committer

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(s)
        b = sorted(t)
        if a == b:
            return True
        return False  