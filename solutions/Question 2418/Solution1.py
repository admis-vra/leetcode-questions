# Problem: 2418. Sort the People
# Difficulty: Easy
# Topics: Array, Hash Table, String, Sorting
# URL: https://leetcode.com/problems/sort-the-people/
# Runtime: 3 ms
# Memory: 18.4 MB
# Solved via CodePath Auto-Committer

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        i = list(range(len(names)))
        i.sort(key=lambda x: heights[x], reverse=True)
        return [names[x] for x in i]