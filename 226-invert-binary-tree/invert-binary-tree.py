# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def fun(s):
            if s is None:
                return s
            s1 = fun(s.right)
            s2 = fun(s.left)
            s.left = s1
            s.right = s2
            return s
        return fun(root)