# Problem: 367. Valid Perfect Square
# Difficulty: Easy
# Topics: Math, Binary Search
# URL: https://leetcode.com/problems/valid-perfect-square/
# Runtime: 0 ms
# Memory: 17.7 MB
# Solved via CodePath Auto-Committer

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <2:
            return True
        l , r = 2, num // 2
        while l <= r:
            mid = (l + r) // 2
            guess = mid * mid
            if guess == num:
                return True
            elif guess < num:
                l = mid + 1
            else:
                r = mid - 1
        return False