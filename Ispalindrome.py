# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Pal:
    def isPalindrome(self, head: ListNode) -> bool:
        if (not head) or (not head.next):
            return True
        out=[]
        while head:
            out.append(head.val)
            head=head.next
        return out==out[::-1]        

a=ListNode(1,ListNode(2,ListNode(2,ListNode(1))))
b=ListNode(2,ListNode(0,ListNode(2)))
c=ListNode(0,ListNode(1))
print(Pal().isPalindrome(a))
print(Pal().isPalindrome(b))
print(Pal().isPalindrome(c))