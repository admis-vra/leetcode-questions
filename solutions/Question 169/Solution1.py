# Problem: 169. Majority Element
# Difficulty: Easy
# Topics: Array, Hash Table, Divide and Conquer, Sorting, Counting, Boyer–Moore Majority Vote Algorithm
# URL: https://leetcode.com/problems/majority-element/
# Runtime: 15 ms
# Memory: 19.4 MB
# Solved via CodePath Auto-Committer

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
            if count[x] > len(nums)//2:
                return x