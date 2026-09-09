# Problem: 88. Merge Sorted Array
# Difficulty: Easy
# Topics: Array, Two Pointers, Sorting
# URL: https://leetcode.com/problems/merge-sorted-array/
# Runtime: 1 ms
# Memory: 18 MB
# Solved via CodePath Auto-Committer

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:m] = nums1[:m]  # optional, just for clarity
        # Merge nums1[:m] and nums2, and sort
        nums1[:m+n] = sorted(nums1[:m] + nums2)