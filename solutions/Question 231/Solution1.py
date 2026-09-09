# Problem: 231. Power of Two
# Difficulty: Easy
# Topics: Math, Bit Manipulation, Recursion
# URL: https://leetcode.com/problems/power-of-two/
# Runtime: 24 ms
# Memory: 17.7 MB
# Solved via CodePath Auto-Committer

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for a in range(200):
            if 2**a == n:
                return True
        return False        
        