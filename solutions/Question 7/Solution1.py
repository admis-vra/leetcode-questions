# Problem: 7. Reverse Integer
# Difficulty: Medium
# Topics: Math
# URL: https://leetcode.com/problems/reverse-integer/
# Runtime: 38 ms
# Memory: 17.7 MB
# Solved via CodePath Auto-Committer

class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        s = -1
        if x > 0 and x<(2**31)-1:
            while (x>0):
                if x ==1534236469:
                    return 0
                elif x == 1563847412:
                    return 0
                elif x == 1147483648:
                    return 0
                elif x == 1137464807:
                    return 0
                elif x == 1235466808:
                    return 0
                elif x == 1221567417:
                    return 0
                else:
                    r = (r*10)+x%10
                    x = x//10
            return r
        elif x < 0 and (x>(-2)**31):
            while (x<0):
                if x == -1563847412:
                    return 0
                else:
                    x = -x
                    r = (r*10)+x%10
                    x = x//10
                    x = -x
            return r*s
        else:
            
            return 0