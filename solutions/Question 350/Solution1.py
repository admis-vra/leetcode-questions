# Problem: 350. Intersection of Two Arrays II
# Difficulty: Easy
# Topics: Array, Hash Table, Two Pointers, Binary Search, Sorting
# URL: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Runtime: 2 ms
# Memory: 17.9 MB
# Solved via CodePath Auto-Committer

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = Counter(nums1)
        b = Counter(nums2) 
        return list((a & b).elements())