# Problem: 9. Palindrome Number
# Difficulty: Easy
# Topics: Math
# URL: https://leetcode.com/problems/palindrome-number/
# Runtime: 13 ms
# Memory: 17.7 MB
# Solved via CodePath Auto-Committer

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0 
        i = x 
        while (i>0):
            rev = (rev*10)+i%10
            i = i//10
        return x==rev
obj = Solution()
print(obj.isPalindrome(121))            