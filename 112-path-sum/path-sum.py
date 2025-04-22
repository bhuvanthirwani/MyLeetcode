# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def fun(root, s):
            
            if root.left == None and root.right == None:
                if s + root.val==targetSum:
                    return True
                return False
            
            s1,s2 = False, False
            if root.left:
                s1=fun(root.left, s+root.val)
            if root.right:
                s2=fun(root.right, s+root.val)
            return s1 or s2
        if root:
            return fun(root, 0) 
        else:
            return False
        