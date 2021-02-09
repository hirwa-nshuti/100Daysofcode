# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Tree:
    def __init__(self):
        self.root=None
    def addNode(self,node,val):
        if (node==None):
            self.root=TreeNode(val)
        else:
            if val<node.data:
                if node.left==None:
                    node.left=TreeNode(val)
                else:
                    self.addNode(node.left,val)
            else:
                if node.right==None:
                    node.right=TreeNode(val)
                else:
                    self.addNode(node.right,val)                
            
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.maximum = 0
        def Order(node)->int:
            if not node: return
                
            Order(node.right)
            node.val+=self.maximum
            self.maximum= node.val
            Order(node.left)
        Order(root)
        return root
