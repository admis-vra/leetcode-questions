# Problem: 27. Remove Element
# Difficulty: Easy
# Topics: Array, Two Pointers
# URL: https://leetcode.com/problems/remove-element/
# Runtime: 0 ms
# Memory: 17.8 MB
# Solved via CodePath Auto-Committer

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
        