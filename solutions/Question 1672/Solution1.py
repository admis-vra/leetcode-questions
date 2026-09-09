# Problem: 1672. Richest Customer Wealth
# Difficulty: Easy
# Topics: Array, Matrix
# URL: https://leetcode.com/problems/richest-customer-wealth/
# Runtime: 0 ms
# Memory: 17.5 MB
# Solved via CodePath Auto-Committer

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts)) # max will  find maximum number
                                       # map will address the location maybe
                                       # sum will add all element together for map