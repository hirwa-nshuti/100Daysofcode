# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        elements = []
        def foo(root,elements):
            if root:
                if root.left:
                    foo(root.left,elements)
                elements.append(root.val)
                if root.right:
                    foo(root.right,elements)
                return elements
            return
        return foo(root,elements)
            