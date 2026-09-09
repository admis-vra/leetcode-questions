# Problem: 58. Length of Last Word
# Difficulty: Easy
# Topics: String
# URL: https://leetcode.com/problems/length-of-last-word/
# Runtime: 0 ms
# Memory: 18 MB
# Solved via CodePath Auto-Committer

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        return len(a[-1])