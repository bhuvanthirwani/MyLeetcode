# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def fun(node, direction, length):
            nonlocal ans
            if node == None:
                return
            ans=max(ans, length)
            r_length = length + 1 if direction=='left' else 1
            l_length = length + 1 if direction=='right' else 1
            fun(node.right, "right", r_length)
            fun(node.left, "left", l_length)
            return
        
        fun(root.left, "left", 1) 
        fun(root.right, "right", 1)
        return ans
            