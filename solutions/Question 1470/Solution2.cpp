/*
 * Problem: 1470. Shuffle the Array
 * Difficulty: Easy
 * Topics: Array
 * URL: https://leetcode.com/problems/shuffle-the-array/
 * Runtime: 0 ms
 * Memory: 13.3 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> ans;
        for(int i = 0;i<n;i++){
            ans.push_back(nums[i]);
            ans.push_back(nums[i+n]);
        }
        return ans;
    }
};