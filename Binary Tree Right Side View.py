# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Right:
    def rightSideView(self, root):
        if not root:
            return []
        
        results, p = [root.val], [root]
        
        while p:
            next = []
            for node in p:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            if next:
                results.append(next[-1].val)
            p = next
        
        return results
a=TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(5,TreeNode(4)))))
print(Right().rightSideView(a))