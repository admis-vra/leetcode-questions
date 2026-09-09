/*
 * Problem: 20. Valid Parentheses
 * Difficulty: Easy
 * Topics: String, Stack, Bracket Sequences
 * URL: https://leetcode.com/problems/valid-parentheses/
 * Runtime: 0 ms
 * Memory: 7.4 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (char c : s) {
            if (c == '(') st.push(')');
            else if (c == '{') st.push('}');
            else if (c == '[') st.push(']');
            else if (st.empty() || st.top() != c) return false;
            else st.pop();
        }
        return st.empty();
    }
};