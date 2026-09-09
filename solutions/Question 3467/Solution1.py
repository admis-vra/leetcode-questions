# Problem: 3467. Transform Array by Parity
# Difficulty: Easy
# Topics: Array, Sorting, Counting
# URL: https://leetcode.com/problems/transform-array-by-parity/
# Runtime: 0 ms
# Memory: 18 MB
# Solved via CodePath Auto-Committer

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for a in range(len(nums)):
            if nums[a] % 2 == 0:
                nums[a] = 0
            else:
                nums[a] = 1
        nums.sort()
        return nums