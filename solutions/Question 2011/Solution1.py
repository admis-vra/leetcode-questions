# Problem: 2011. Final Value of Variable After Performing Operations
# Difficulty: Easy
# Topics: Array, String, Simulation
# URL: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# Runtime: 0 ms
# Memory: 17.7 MB
# Solved via CodePath Auto-Committer

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        c = 0
        for a in operations:
            if a == "--X" or a == "X--":
                c -= 1
            elif a == "X++" or a == "++X":
                c += 1
            else: continue
        return c