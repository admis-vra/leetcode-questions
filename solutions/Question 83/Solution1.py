# Problem: 83. Remove Duplicates from Sorted List
# Difficulty: Easy
# Topics: Linked List
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Runtime: 0 ms
# Memory: 17.8 MB
# Solved via CodePath Auto-Committer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = head
        while r and r.next:
            if r.val == r.next.val:
                r.next = r.next.next
            else:
                r = r.next
        return head
        