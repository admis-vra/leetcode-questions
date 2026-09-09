# Problem: 70. Climbing Stairs
# Difficulty: Easy
# Topics: Math, Dynamic Programming, Memoization
# URL: https://leetcode.com/problems/climbing-stairs/
# Runtime: 0 ms
# Memory: 17.6 MB
# Solved via CodePath Auto-Committer

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2  # ways(1), ways(2)
        for _ in range(3, n+1):
                a, b = b, a+b
        return b
        