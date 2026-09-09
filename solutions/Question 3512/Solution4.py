# Problem: 3512. Minimum Operations to Make Array Sum Divisible by K
# Difficulty: Easy
# Topics: Array, Math
# URL: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
# Runtime: 0 ms
# Memory: 18.1 MB
# Solved via CodePath Auto-Committer

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x=sum(nums)
        if x%k==0:
            return 0
        else:
            if ((x%k)+x)%k==0:
                return k-(x%k)
            else:
                return x%k
        