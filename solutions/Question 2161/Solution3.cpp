/*
 * Problem: 2161. Partition Array According to Given Pivot
 * Difficulty: Medium
 * Topics: Array, Two Pointers, Simulation
 * URL: https://leetcode.com/problems/partition-array-according-to-given-pivot/
 * Runtime: 0 ms
 * Memory: 133.4 MB
 * Solved via CodePath Auto-Committer
 */

// class Solution {
// public:
//     vector<int> pivotArray(vector<int>& nums, int pivot) {
//         vector<int> ans;
//         for(int i = 0;i<nums.size();i++){
//             if(nums[i] < pivot){
//                 ans.push_back(nums[i]);
//             }
//         }
//         for(int i = 0;i<nums.size();i++){
//             if(nums[i] == pivot){
//                 ans.push_back(nums[i]);
//             }
//         }
//         for(int i = 0;i<nums.size();i++){
//             if(nums[i] > pivot){
//                 ans.push_back(nums[i]);
//             }
//         }

//         return ans;

//     }
// };

// my solution but 10-15 mx rumtime;


//top solution
class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> ans;
        int idx = 0;
        for(int x : nums){
            if(x < pivot){
                ans.push_back(x);
            }
            if( x == pivot) idx++;
        }
        for(int i = 0;i<idx;i++){   
            ans.push_back(pivot);
        }
        for(int i : nums){
            if(i > pivot){
                ans.push_back(i);
            }
        }

        return ans;

    }
};