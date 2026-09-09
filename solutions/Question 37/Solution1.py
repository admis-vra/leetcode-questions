# Problem: 37. Sudoku Solver
# Difficulty: Hard
# Topics: Array, Hash Table, Backtracking, Matrix, Algorithm X, Dancing Links
# URL: https://leetcode.com/problems/sudoku-solver/
# Runtime: 1207 ms
# Memory: 17.8 MB
# Solved via CodePath Auto-Committer

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize sets with existing numbers
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empty.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(i=0):
            if i == len(empty):  # all filled
                return True
            r, c = empty[i]
            b = (r // 3) * 3 + (c // 3)

            for ch in "123456789":
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[b]:
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[b].add(ch)

                    if backtrack(i + 1):
                        return True

                    # undo
                    board[r][c] = "."
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[b].remove(ch)

            return False

        backtrack()
