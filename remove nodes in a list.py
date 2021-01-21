# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)
            

class removeNode(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val,node.next=node.next.val, node.next.next 

if __name__=="__main__":
    list_node=ListNode(1,ListNode(4,ListNode(0)))
    y=removeNode(list_node[1])
    print(y)