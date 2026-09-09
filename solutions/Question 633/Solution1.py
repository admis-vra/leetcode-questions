# Problem: 633. Sum of Square Numbers
# Difficulty: Medium
# Topics: Math, Two Pointers, Binary Search
# URL: https://leetcode.com/problems/sum-of-square-numbers/
# Runtime: 43 ms
# Memory: 17.7 MB
# Solved via CodePath Auto-Committer

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.sqrt(c))
        
        while a <= b:
            curr = a * a + b * b
            if curr == c:
                return True
            elif curr < c:
                a += 1
            else:
                b -= 1
        return False
