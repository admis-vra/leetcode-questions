# Problem: 1470. Shuffle the Array
# Difficulty: Easy
# Topics: Array
# URL: https://leetcode.com/problems/shuffle-the-array/
# Runtime: 58 ms
# Memory: 17.8 MB
# Solved via CodePath Auto-Committer

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = []
        for a in range(n):
            x.append(nums[a])
            x.append(nums[a+n])
        return x