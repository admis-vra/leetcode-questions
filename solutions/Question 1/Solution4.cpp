/*
 * Problem: 1. Two Sum
 * Difficulty: Easy
 * Topics: Array, Hash Table
 * URL: https://leetcode.com/problems/two-sum/
 * Runtime: 71 ms
 * Memory: 14.1 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int x = 0;
        vector<int> ans;
        for(int i = 0;i<nums.size();i++){
            for(int j = i+1 ; j<nums.size();j++){
                if(nums[i]+nums[j] == target){
                    ans.push_back(i);
                    ans.push_back(j);
                    x++;
                    break;
                }
            }
            if(x) break;
        }
        return ans;
    }
};