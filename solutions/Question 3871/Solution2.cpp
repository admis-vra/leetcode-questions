/*
 * Problem: 3871. Count Commas in Range II
 * Difficulty: Medium
 * Topics: Math
 * URL: https://leetcode.com/problems/count-commas-in-range-ii/
 * Runtime: 0 ms
 * Memory: 8.9 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    long long countCommas(long long n) {
        long long count = 0;
        if (n >= 1000) count += n - 999;
        if (n >= 1000000LL) count += n - 999999LL;
        if (n >= 1000000000LL) count += n - 999999999LL;
        if (n >= 1000000000000LL) count += n - 999999999999LL;
        if (n >= 1000000000000000LL) count += n - 999999999999999LL;
        
        return count;

        
    }
};