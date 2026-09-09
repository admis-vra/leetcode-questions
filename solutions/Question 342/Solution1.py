# Problem: 342. Power of Four
# Difficulty: Easy
# Topics: Math, Bit Manipulation, Recursion
# URL: https://leetcode.com/problems/power-of-four/
# Runtime: 0 ms
# Memory: 17.8 MB
# Solved via CodePath Auto-Committer

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            x=math.log(n, 4)
        return True if n==4**round(x) else False  