# Problem: 35. Search Insert Position
# Difficulty: Easy
# Topics: Array, Binary Search
# URL: https://leetcode.com/problems/search-insert-position/
# Runtime: 0 ms
# Memory: 18.5 MB
# Solved via CodePath Auto-Committer

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)