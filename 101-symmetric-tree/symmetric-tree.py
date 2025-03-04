# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def fun(root1, root2):
            if root1 == None and root2 == None: 
                return True
            if root1 == None or root2 == None:
                return False
            if root1 and root2:
                r1 = fun(root1.left, root2.right)
                r2 = fun(root1.right, root2.left)
                return r1 and r2 and root1.val == root2.val
            return False
        return fun(root, root)