# Problem: 125. Valid Palindrome
# Difficulty: Easy
# Topics: Two Pointers, String
# URL: https://leetcode.com/problems/valid-palindrome/
# Runtime: 7 ms
# Memory: 19.3 MB
# Solved via CodePath Auto-Committer

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return cleaned == cleaned[::-1]

a = Solution()
print(a.isPalindrome("race car"))