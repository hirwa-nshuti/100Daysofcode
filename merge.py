# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode() 
        curr = head
        while True: 
            if not l1: 
                curr.next = l2 
                break
            if not l2: 
                curr.next = l1
                break
            if l1.val <= l2.val: 
                curr.next = l1 
                l1 = l1.next
            else: 
                curr.next = l2 
                l2 = l2.next
            curr = curr.next

        return head.next
a = ListNode(1, ListNode(2, ListNode(4, ListNode(7))))
b = ListNode(1, ListNode(3, ListNode(4, ListNode(6, ListNode(7)))))



print(Solution().mergeTwoLists(a, b))