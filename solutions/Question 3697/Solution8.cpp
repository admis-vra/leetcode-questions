/*
 * Problem: 3697. Compute Decimal Representation
 * Difficulty: Easy
 * Topics: Array, Math
 * URL: https://leetcode.com/problems/compute-decimal-representation/
 * Runtime: 0 ms
 * Memory: 9.5 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    vector<int> decimalRepresentation(int n) {
        long long num = 1;
        vector<int> ans;
        while(n>0){
            int x = n%10;
            x *= num;
            num *= 10;
            if(x != 0)
                ans.push_back(x);
            n = n/10;
        }
        reverse(ans.begin(),ans.end());
        return ans;
        
    }
};