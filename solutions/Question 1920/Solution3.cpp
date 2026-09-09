/*
 * Problem: 1920. Build Array from Permutation
 * Difficulty: Easy
 * Topics: Array, Simulation
 * URL: https://leetcode.com/problems/build-array-from-permutation/
 * Runtime: 0 ms
 * Memory: 20.7 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> ans;
        for(int x:nums){
            ans.push_back(nums[x]);
        }
        return ans;
    }
};