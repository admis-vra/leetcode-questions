/*
 * Problem: 2161. Partition Array According to Given Pivot
 * Difficulty: Medium
 * Topics: Array, Two Pointers, Simulation
 * URL: https://leetcode.com/problems/partition-array-according-to-given-pivot/
 * Runtime: 14 ms
 * Memory: 139.1 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> before;
        vector<int> pivot_vector;
        vector<int> after;
        for(int i = 0;i<nums.size();i++){
            if(nums[i] < pivot){
                before.push_back(nums[i]);
            }
        }
        for(int i = 0;i<nums.size();i++){
            if(nums[i] == pivot){
                pivot_vector.push_back(nums[i]);
            }
        }
        for(int i = 0;i<nums.size();i++){
            if(nums[i] > pivot){
                after.push_back(nums[i]);
            }
        }
        before.insert(before.end(),pivot_vector.begin(),pivot_vector.end());
        before.insert(before.end(),after.begin(),after.end());

        return before;

    }
};