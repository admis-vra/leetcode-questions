/*
 * Problem: 217. Contains Duplicate
 * Difficulty: Easy
 * Topics: Array, Hash Table, Sorting
 * URL: https://leetcode.com/problems/contains-duplicate/
 * Runtime: 73 ms
 * Memory: 111.4 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for(int x : nums){
            if(seen.count(x)) return true;
            seen.insert(x);
        }
        return false;
    }
};