# Problem: 66. Plus One
# Difficulty: Easy
# Topics: Array, Math
# URL: https://leetcode.com/problems/plus-one/
# Runtime: 0 ms
# Memory: 17.6 MB
# Solved via CodePath Auto-Committer

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits))) + 1
        return [int(d) for d in str(num)]