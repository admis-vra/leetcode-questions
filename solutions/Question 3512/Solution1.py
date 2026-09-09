# Problem: 3512. Minimum Operations to Make Array Sum Divisible by K
# Difficulty: Easy
# Topics: Array, Math
# URL: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
# Runtime: 0 ms
# Memory: 17.8 MB
# Solved via CodePath Auto-Committer

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x=sum(nums)
        return x%k
        