# Problem: 28. Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Topics: Two Pointers, String, String Matching, Z Algorithm, Knuth–Morris–Pratt Algorithm, Boyer–Moore String-Search Algorithm
# URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Runtime: 0 ms
# Memory: 17.7 MB
# Solved via CodePath Auto-Committer

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else: return -1
        