/*
 * Problem: 3697. Compute Decimal Representation
 * Difficulty: Easy
 * Topics: Array, Math
 * URL: https://leetcode.com/problems/compute-decimal-representation/
 * Runtime: 3 ms
 * Memory: 9.7 MB
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
            num *= 10; // giving error if num is int;
            if(x != 0)
                ans.push_back(x);
            n = n/10;
        }
        reverse(ans.begin(),ans.end()); // we can also just sort reverse;
        // sort(ans.rbegin(),ans.rend()); // but after this runtine is 3ms not 0 
        return ans;  
        
    }
};