# Problem: 326. Power of Three
# Difficulty: Easy
# Topics: Math, Recursion
# URL: https://leetcode.com/problems/power-of-three/
# Runtime: 25 ms
# Memory: 17.7 MB
# Solved via CodePath Auto-Committer

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for a in range(0,20):
            if 3**a == n:
                return True
        return False
        