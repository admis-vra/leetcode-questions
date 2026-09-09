/*
 * Problem: 1672. Richest Customer Wealth
 * Difficulty: Easy
 * Topics: Array, Matrix
 * URL: https://leetcode.com/problems/richest-customer-wealth/
 * Runtime: 0 ms
 * Memory: 11.4 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int richest= 0;
        for (const auto& row : accounts) {
            int sum = accumulate(row.begin(), row.end(), 0) ;
            if (sum >= richest) richest = sum;
        }
        return richest;

        
    }
};