# Problem: 3005. Count Elements With Maximum Frequency
# Difficulty: Easy
# Topics: Array, Hash Table, Counting
# URL: https://leetcode.com/problems/count-elements-with-maximum-frequency/
# Runtime: 3 ms
# Memory: 17.8 MB
# Solved via CodePath Auto-Committer

from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)  # frequency of each element
        max_freq = max(freq.values())  # maximum frequency
        count = sum(v for v in freq.values() if v == max_freq)  # sum of elements with max freq
        return count
