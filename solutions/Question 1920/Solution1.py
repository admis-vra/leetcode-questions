# Problem: 1920. Build Array from Permutation
# Difficulty: Easy
# Topics: Array, Simulation
# URL: https://leetcode.com/problems/build-array-from-permutation/
# Runtime: 0 ms
# Memory: 18.1 MB
# Solved via CodePath Auto-Committer

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return[nums[num] for num in nums]
