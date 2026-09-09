# Problem: 136. Single Number
# Difficulty: Easy
# Topics: Array, Bit Manipulation
# URL: https://leetcode.com/problems/single-number/
# Runtime: 0 ms
# Memory: 19.6 MB
# Solved via CodePath Auto-Committer

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for num in nums:
            r ^= num  #XOR 
        return r