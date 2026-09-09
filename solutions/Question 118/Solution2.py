# Problem: 118. Pascal's Triangle
# Difficulty: Easy
# Topics: Array, Dynamic Programming
# URL: https://leetcode.com/problems/pascals-triangle/
# Runtime: 0 ms
# Memory: 18 MB
# Solved via CodePath Auto-Committer

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)

        return triangle
