# Definition for singly-linked list.

class ListNode:
        def __init__(self, x,next=None):
            self.val = x
            self.next = None
        def __repr__(self):
            if self:
                return "{} -> {}".format(self.val, self.next)
   

class cycle:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        else:
            while head!=None:
                if(head.val == ''):
                    return True
                else:
                    head.val = ''
                head = head.next
            return False


x=ListNode(1,ListNode(4,ListNode(2,ListNode(0,ListNode(-2,ListNode(-4))))))
y=ListNode(3,ListNode(2,ListNode(0,ListNode(-4))))
print(cycle().hasCycle(x))
print(cycle().hasCycle(y))