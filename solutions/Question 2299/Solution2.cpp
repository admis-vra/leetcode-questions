/*
 * Problem: 2299. Strong Password Checker II
 * Difficulty: Easy
 * Topics: String
 * URL: https://leetcode.com/problems/strong-password-checker-ii/
 * Runtime: 0 ms
 * Memory: 8.2 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    bool strongPasswordCheckerII(string password) {
        if(password.size() < 8) return false;
        bool adjacent = false;
        bool upper = false;
        bool lower = false;
        bool digit = false;
        bool special = false;
        for (char c : password) {
            if (isupper(c)) upper = true;
            else if (islower(c)) lower = true;
            else if (isdigit(c)) digit = true;
            else if (ispunct(c)) special = true;
        }
        for (size_t i = 0; i < password.length() - 1; ++i) {
            if (password[i] == password[i + 1]) {
                adjacent = true;
                break;
            }
        }
        return (!adjacent && special && digit && upper && lower);
    }
};