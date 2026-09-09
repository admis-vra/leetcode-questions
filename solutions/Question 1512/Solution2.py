# Problem: 1512. Number of Good Pairs
# Difficulty: Easy
# Topics: Array, Hash Table, Math, Counting
# URL: https://leetcode.com/problems/number-of-good-pairs/
# Runtime: 3 ms
# Memory: 17.9 MB
# Solved via CodePath Auto-Committer

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                if nums[a] == nums[b]: c += 1
        return c


        