/*
 * Problem: 283. Move Zeroes
 * Difficulty: Easy
 * Topics: Array, Two Pointers
 * URL: https://leetcode.com/problems/move-zeroes/
 * Runtime: 0 ms
 * Memory: 24.9 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int count = 0;
        vector<int> ans;
        for(int x:nums){
            if (x == 0) count++;
            else ans.push_back(x);
        }
        for(int i = 0;i<count;i++){
            ans.push_back(0);
        }
        nums = ans;;
        
    }
};