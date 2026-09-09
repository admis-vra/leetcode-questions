/*
 * Problem: 1480. Running Sum of 1d Array
 * Difficulty: Easy
 * Topics: Array, Prefix Sum
 * URL: https://leetcode.com/problems/running-sum-of-1d-array/
 * Runtime: 0 ms
 * Memory: 12.5 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> ans;
        int num = 0;
        for(int x: nums){
            num = num + x;
            ans.push_back(num);
        }
        return ans;
    }
};