# Problem: 258. Add Digits
# Difficulty: Easy
# Topics: Math, Simulation, Number Theory
# URL: https://leetcode.com/problems/add-digits/
# Runtime: 0 ms
# Memory: 17.9 MB
# Solved via CodePath Auto-Committer

class Solution:
    def addDigits(self, num: int) -> int:
        a = num
        while a>9:
            a=0
            while num>0:
                a+=num%10
                num = num//10
            num = a
        return a
        