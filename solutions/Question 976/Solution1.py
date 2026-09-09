# Problem: 976. Largest Perimeter Triangle
# Difficulty: Easy
# Topics: Array, Math, Greedy, Sorting, Quicksort, Polygons
# URL: https://leetcode.com/problems/largest-perimeter-triangle/
# Runtime: 16 ms
# Memory: 18.7 MB
# Solved via CodePath Auto-Committer

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(len(nums)-1, 1, -1):
            if nums[x-2] + nums[x-1] > nums[x]:
                return nums[x-2] + nums[x-1] + nums[x]
        return 0