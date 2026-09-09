# Problem: 69. Sqrt(x)
# Difficulty: Easy
# Topics: Math, Binary Search, Newton's Method
# URL: https://leetcode.com/problems/sqrtx/
# Runtime: 1 ms
# Memory: 18 MB
# Solved via CodePath Auto-Committer

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid
            if mid_squared == x:
                return mid 
            elif mid_squared < x:
                left = mid + 1 
            else:
                right = mid - 1  
        
        return right  