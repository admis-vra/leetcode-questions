/*
 * Problem: 1823. Find the Winner of the Circular Game
 * Difficulty: Medium
 * Topics: Array, Math, Recursion, Queue, Simulation
 * URL: https://leetcode.com/problems/find-the-winner-of-the-circular-game/
 *
 * Description:
 * There are `n` friends that are playing a game. The friends are sitting in a circle and are numbered from `1` to `n` in **clockwise order**. More formally, moving clockwise from the `ith` friend brings you to the `(i+1)th` friend for `1 th` friend brings you to the `1st` friend.
 * 
 * The rules of the game are as follows:
 * 
 * 	
 * - **Start** at the `1st` friend.
 * 	
 * - Count the next `k` friends in the clockwise direction **including** the friend you started at. The counting wraps around the circle and may count some friends more than once.
 * 	
 * - The last friend you counted leaves the circle and loses the gam
 * Solved via CodePath Auto-Committer
 */

// Solution for Find the Winner of the Circular Game
// Solved on LeetCode