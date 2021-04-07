# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        elements = []
        def preor(root,elements):
            if root:
                elements.append(root.val)
                if root.left:
                    preor(root.left,elements)
                if root.right:
                    preor(root.right,elements)
            return elements
        return preor(root,elements)
                