/*
 * Problem: 1. Two Sum
 * Difficulty: Easy
 * Topics: Array, Hash Table
 * URL: https://leetcode.com/problems/two-sum/
 * Runtime: 52 ms
 * Memory: 17.2 MB
 * Solved via CodePath Auto-Committer
 */

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []