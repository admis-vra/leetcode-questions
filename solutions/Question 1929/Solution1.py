# Problem: 1929. Concatenation of Array
# Difficulty: Easy
# Topics: Array, Simulation
# URL: https://leetcode.com/problems/concatenation-of-array/
# Runtime: 0 ms
# Memory: 17.8 MB
# Solved via CodePath Auto-Committer

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums 