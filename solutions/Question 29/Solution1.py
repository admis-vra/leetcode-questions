# Problem: 29. Divide Two Integers
# Difficulty: Medium
# Topics: Math, Bit Manipulation
# URL: https://leetcode.com/problems/divide-two-integers/
# Runtime: 0 ms
# Memory: 18 MB
# Solved via CodePath Auto-Committer

class Solution:
    def divide(self,dividend: int, divisor: int) -> int:
        imax = 2**31 - 1
        imin = -2**31
    
        # Handle overflow case
        if dividend == imin and divisor == -1:
            return imax
        result = int(dividend / divisor)       
        return result
        
        