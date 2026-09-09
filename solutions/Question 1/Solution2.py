# Problem: 1. Two Sum
# Difficulty: Easy
# Topics: Array, Hash Table
# URL: https://leetcode.com/problems/two-sum/
# Runtime: 2049 ms
# Memory: 13.3 MB
# Solved via CodePath Auto-Committer

class Solution(object):
    def twoSum(self, nums, target):
        for a in range(len(nums)): #range(4) for nums = [2,7,11,15]
            for b in range(a+1, len(nums)): # a=0 range(4), a=1 range(1,4), a=2 range(2,4), a=3 range(3,4), a=4 range(4,4)(no loop),
                if nums[a] + nums[b] == target: # my traget is 9 for that list
                    return [a,b] #this is to return index not value