/*
 * Problem: 1. Two Sum
 * Difficulty: Easy
 * Topics: Array, Hash Table
 * URL: https://leetcode.com/problems/two-sum/
 * Runtime: 0 ms
 * Memory: 14.8 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        

        int found = 0;
        int i = 0;
        int j = nums.size()-1;
        vector<pair<int,int>> num(nums.size());
        for(int i = 0;i<nums.size();i++){
            num[i].first = nums[i];
            num[i].second = i;
        }
        sort(num.begin(),num.end());
        while (i < j) {
            int sum = num[i].first + num[j].first;

            if (sum == target) {
                return {num[i].second, num[j].second};
            }
            else if (sum < target) {
                i++;
            }
            else {
                j--;
            }
        }    
        return {};
    }   
};