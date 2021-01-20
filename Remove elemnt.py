'''Remove all elements from a linked list of integers that have value val.
Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)
            
class RemoveEL:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr=head
        pre=head
        while curr:
            if (curr.val==val) and curr==head:
                head=head.next
            elif curr.val==val and curr!=head:
                pre.next=curr.next
                curr=curr.next
            else:
                pre=curr
                curr=curr.next
        return head

a=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))
b=5

print("Before removing the element B: ",a)
print("After removing the element B: ",RemoveEL().removeElements(a,b))
