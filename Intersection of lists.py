#Definition for singly-linked list.\

class ListNode:
        def __init__(self, x,next=None):
            self.val = x
            self.next = None
        def __repr__(self):
            if self:
                return "{} -> {}".format(self.val, self.next)

class Intersecs:
    def getIntersectionNode(self,  headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        a=headA
        b=headB
        while (a!=b):
            if a==None:
                a=headB
            else:
                a=a.next
            if b==None:
                b=headA
            else:
                b=b.next
        
        return a

a=ListNode(1,ListNode(2,ListNode(5,ListNode(8,ListNode(5,ListNode(4))))))
b=ListNode(6,ListNode(8,ListNode(5,ListNode(4))))
print(Intersecs().getIntersectionNode(a,b))