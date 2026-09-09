# Problem: 2000. Reverse Prefix of Word
# Difficulty: Easy
# Topics: Two Pointers, String, Stack
# URL: https://leetcode.com/problems/reverse-prefix-of-word/
# Runtime: 0 ms
# Memory: 17.9 MB
# Solved via CodePath Auto-Committer

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        m = word.find(ch)
        if ch in word:
            a = word[m::-1]+word[m+1:]
            return a
        else :
            return word