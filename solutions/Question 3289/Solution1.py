# Problem: 3289. The Two Sneaky Numbers of Digitville
# Difficulty: Easy
# Topics: Array, Hash Table, Math
# URL: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
# Runtime: 7 ms
# Memory: 17.8 MB
# Solved via CodePath Auto-Committer

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a = []
        for x in nums:
            m = nums.count(x) 
            if m == 2:
                a.append(x)
        a = set(a)
        a = list(a)
        return a