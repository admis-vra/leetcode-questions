# Problem: 3190. Find Minimum Operations to Make All Elements Divisible by Three
# Difficulty: Easy
# Topics: Array, Math
# URL: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
# Runtime: 0 ms
# Memory: 17.8 MB
# Solved via CodePath Auto-Committer

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0
        for a in nums:
            if a%3 != 0:
                c += 1
        return c
        