/*
 * Problem: 20. Valid Parentheses
 * Difficulty: Easy
 * Topics: String, Stack, Bracket Sequences
 * URL: https://leetcode.com/problems/valid-parentheses/
 * Runtime: 0 ms
 * Memory: 7.4 MB
 *
 * Description:
 * Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
 * 
 * An input string is valid if:
 * 
 * 	
 * - Open brackets must be closed by the same type of brackets.
 * 	
 * - Open brackets must be closed in the correct order.
 * 	
 * - Every close bracket has a corresponding open bracket of the same type.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** s = "()"
 * 
 * **Output:** true
 * 
 * **Example 2:**
 * 
 * **Input:** s = "()[]{}"
 * 
 * **Output:** true
 * 
 * **Example 3:**
 * 
 * **Input:** s = "(]"
 * 
 * **Output:** false
 * 
 * **Example 4:**
 * 
 * **Input:** s = "([])"
 * 
 * **Output:** true
 * 
 * **Example 
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