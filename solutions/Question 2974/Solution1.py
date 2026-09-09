# Problem: 2974. Minimum Number Game
# Difficulty: Easy
# Topics: Array, Sorting, Heap (Priority Queue), Simulation
# URL: https://leetcode.com/problems/minimum-number-game/
# Runtime: 4 ms
# Memory: 17.6 MB
# Solved via CodePath Auto-Committer

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for a in range (0, len(nums)-1,2):
            nums[a] , nums[a+1] = nums[a+1], nums[a]
        return nums