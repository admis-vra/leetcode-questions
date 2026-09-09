# Problem: 3005. Count Elements With Maximum Frequency
# Difficulty: Easy
# Topics: Array, Hash Table, Counting
# URL: https://leetcode.com/problems/count-elements-with-maximum-frequency/
# Runtime: 0 ms
# Memory: 17.9 MB
# Solved via CodePath Auto-Committer

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums) 
        max_freq = max(freq.values()) 
        count = sum(v for v in freq.values() if v == max_freq)  
        return count
