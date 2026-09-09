# Problem: 88. Merge Sorted Array
# Difficulty: Easy
# Topics: Array, Two Pointers, Sorting
# URL: https://leetcode.com/problems/merge-sorted-array/
# Runtime: 0 ms
# Memory: 17.8 MB
# Solved via CodePath Auto-Committer

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:m+n] = sorted(nums1[:m] + nums2)