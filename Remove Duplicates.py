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
        curr=head
        while curr and curr.next:
            if curr.val==curr.next.val:
                curr.next=curr.next.next
            else:
                curr=curr.next
           
        return head



a=ListNode(1,ListNode(2,ListNode(2,ListNode(4,ListNode(5)))))
b=ListNode(0,ListNode(2,ListNode(3, ListNode(3))))
c=ListNode(1,ListNode(1,ListNode(4)))
d=ListNode(1,ListNode(1,ListNode(1)))
e=ListNode(2,ListNode(3,ListNode(3)))

print("Before removing duplicates",a)
print("Removed Duplicates from A \n")
print(Duplicates().deleteDuplicates(a))
print("Before removing duplicates",b)
print("Removed Duplicates from B \n")
print(Duplicates().deleteDuplicates(b))
print("Before removing duplicates",c)
print("Removed Duplicates from C \n")
print(Duplicates().deleteDuplicates(c))
print("Before removing duplicates",d)
print("Removed Duplicates from D \n")
print(Duplicates().deleteDuplicates(d))
print("Before removing duplicates",e)
print("Removed Duplicates from E \n")
print(Duplicates().deleteDuplicates(e))            
        
                
        