# Problem: 349. Intersection of Two Arrays
# Difficulty: Easy
# Topics: Array, Hash Table, Two Pointers, Binary Search, Sorting
# URL: https://leetcode.com/problems/intersection-of-two-arrays/
# Runtime: 0 ms
# Memory: 18 MB
# Solved via CodePath Auto-Committer

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(nums2))