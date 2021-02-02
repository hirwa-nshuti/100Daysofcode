# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        if self:
            return "{} -> {} -> {}".format(self.val,self.left, self.right)
class Trim:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        while root:
            if root.val < low: root = root.right
            elif root.val > high: root = root.left
            else: break
        
    
        ref = TreeNode(left=root, right=root)
        # Low state
        prev, cur = ref, root
        while cur:
            if cur.val > low:
                prev, cur = cur, cur.left
            elif cur.val < low:
                prev.left = cur = cur.right
            else:
                cur.left = None
                break
         #high state
        prev, cur = ref, root
        while cur:
            if cur.val < high:
                prev, cur = cur, cur.right
            elif cur.val > high:
                prev.right = cur = cur.left
            else:
                cur.right = None
                break       
        return root
a=TreeNode(1)
low=1
high=2
print("The Binary Tree is: ",a)
print(Trim().trimBST(a,low,high))