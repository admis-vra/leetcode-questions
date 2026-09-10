/*
 * Problem: 2161. Partition Array According to Given Pivot
 * Difficulty: Medium
 * Topics: Array, Two Pointers, Simulation
 * URL: https://leetcode.com/problems/partition-array-according-to-given-pivot/
 * Runtime: 15 ms
 * Memory: 133.5 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> before;
        for(int i = 0;i<nums.size();i++){
            if(nums[i] < pivot){
                before.push_back(nums[i]);
            }
        }
        for(int i = 0;i<nums.size();i++){
            if(nums[i] == pivot){
                before.push_back(nums[i]);
            }
        }
        for(int i = 0;i<nums.size();i++){
            if(nums[i] > pivot){
                before.push_back(nums[i]);
            }
        }

        return before;

    }
};