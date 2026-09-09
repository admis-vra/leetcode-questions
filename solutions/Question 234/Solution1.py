# Problem: 234. Palindrome Linked List
# Difficulty: Easy
# Topics: Linked List, Two Pointers, Stack, Recursion
# URL: https://leetcode.com/problems/palindrome-linked-list/
# Runtime: 19 ms
# Memory: 39.2 MB
# Solved via CodePath Auto-Committer

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]


def build_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for x in lst:
        current.next = ListNode(x)
        current = current.next
    return dummy.next

obj = Solution()
print(obj.isPalindrome(build_linked_list([1,2,2,1])))  
print(obj.isPalindrome(build_linked_list([1,2])))      
