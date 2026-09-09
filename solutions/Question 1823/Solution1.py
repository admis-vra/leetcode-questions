# Problem: 1823. Find the Winner of the Circular Game
# Difficulty: Medium
# Topics: Array, Math, Recursion, Queue, Simulation
# URL: https://leetcode.com/problems/find-the-winner-of-the-circular-game/
# Runtime: 103 ms
# Memory: 17.7 MB
# Solved via CodePath Auto-Committer

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()

        for i in range(1,n+1):
            q.append(i)
        while len(q)>1:
            for i in range(k-1):
                n = q.popleft()
                q.append(n)
            q.popleft()
        return q[0]
        