/*
 * Problem: 206. Reverse Linked List
 * Difficulty: Easy
 * Topics: Linked List, Recursion
 * URL: https://leetcode.com/problems/reverse-linked-list/
 * Runtime: 0 ms
 * Memory: 13.4 MB
 * Solved via CodePath Auto-Committer
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* first = nullptr;
        ListNode* last = head;
        while (last != nullptr) {
            ListNode* temp = last->next; 
            last->next = first;
            first = last;
            last = temp;
        }
        return first;
    }
};