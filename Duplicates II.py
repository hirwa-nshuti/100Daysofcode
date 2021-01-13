# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)
class Duplicates:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        empty = None
        while curr and curr.next: 
            if curr.val == curr.next.val: 
                while (curr and curr.next and curr.val == curr.next.val): 
                    curr = curr.next
                curr =curr.next
                if empty is None:
                    head =curr
                else:
                    empty.next = curr
            else:
                empty = curr
                curr = curr.next
        return head

a=ListNode(1,ListNode(2,ListNode(2,ListNode(3))))
b=ListNode(3,ListNode(0,ListNode(4,ListNode(4))))
c=ListNode(1,ListNode(1))
print(Duplicates().deleteDuplicates(a))
print(Duplicates().deleteDuplicates(b))
print(Duplicates().deleteDuplicates(c))