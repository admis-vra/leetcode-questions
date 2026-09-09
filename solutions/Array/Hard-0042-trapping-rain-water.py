/*
 * Problem: 42. Trapping Rain Water
 * Difficulty: Hard
 * Topics: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
 * URL: https://leetcode.com/problems/trapping-rain-water/
 * Runtime: 98 ms
 * Memory: 18.9 MB
 * Solved via CodePath Auto-Committer
 */

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        ans = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_max: l_max = height[l]
                else: ans += l_max - height[l]
                l += 1
            else:
                if height[r] >= r_max: r_max = height[r]
                else: ans += r_max - height[r]
                r -= 1
        return ans