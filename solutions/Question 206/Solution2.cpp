/*
 * Problem: 206. Reverse Linked List
 * Difficulty: Easy
 * Topics: Linked List, Recursion
 * URL: https://leetcode.com/problems/reverse-linked-list/
 * Runtime: 0 ms
 * Memory: 13.3 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr != nullptr) {
            ListNode* temp = curr->next; 
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }
};