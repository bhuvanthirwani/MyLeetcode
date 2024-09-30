# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        D={}
        global max_level
        max_level = 0
        def fun(root, level):
            global max_level
            if root == None:
                return None
            if level in D:
                D[level] += root.val
            else:
                D[level] = root.val
            max_level = max(max_level, level)
            fun(root.left, level + 1)
            fun(root.right, level + 1)
            return
        
        fun(root, 1)
        ans = -1
        max_sum = -999999999999999999999
        for level in range(1, max_level+1):
            if D[level] > max_sum:
                max_sum = D[level]
                ans = level
        return ans