/*
 * Problem: 3870. Count Commas in Range
 * Difficulty: Easy
 * Topics: Math
 * URL: https://leetcode.com/problems/count-commas-in-range/
 * Runtime: 0 ms
 * Memory: 8.5 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    int countCommas(int n) {
        if(n>= 1000) return n-999;
        return 0;
    }
};