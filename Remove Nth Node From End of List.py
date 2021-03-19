"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = []
        
        while(head):
            l.append(head.val)
            head = head.next
        
        l.pop(len(l)-n)
        i = ListNode()
        temp = i
        for j in l:
            i.next = ListNode(j)
            i = i.next
        return temp.next
