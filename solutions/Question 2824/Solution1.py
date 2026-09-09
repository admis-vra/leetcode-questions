# Problem: 2824. Count Pairs Whose Sum is Less than Target
# Difficulty: Easy
# Topics: Array, Two Pointers, Binary Search, Sorting
# URL: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
# Runtime: 7 ms
# Memory: 17.9 MB
# Solved via CodePath Auto-Committer

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = []
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                if nums[a] + nums[b] < target:
                    n.append([nums[a], nums[b]])
        return len(n)        