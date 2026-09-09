# Problem: 9. Palindrome Number
# Difficulty: Easy
# Topics: Math
# URL: https://leetcode.com/problems/palindrome-number/
# Runtime: 0 ms
# Memory: 17.9 MB
# Solved via CodePath Auto-Committer

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0 
        i = x 
        while (i>0):
            rev = (rev*10)+i%10
            i = i//10
        return x==rev
        