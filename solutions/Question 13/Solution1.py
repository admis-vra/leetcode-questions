# Problem: 13. Roman to Integer
# Difficulty: Easy
# Topics: Hash Table, Math, String
# URL: https://leetcode.com/problems/roman-to-integer/
# Runtime: 7 ms
# Memory: 17.9 MB
# Solved via CodePath Auto-Committer

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    
        total = 0
        i = 0
    
        while i < len(s):
            # If this is not the last char and smaller than next → subtract
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2  # skip both
            else:
                total += values[s[i]]
                i += 1
        return total