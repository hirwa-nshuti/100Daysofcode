# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        elements = []
        def foo(root,elements):
            if root.left:
                foo(root.left,elements)
            if root.right:
                foo(root.right,elements)
            elements.append(root.val)
            
            return elements
        return foo(root,elements)
            