# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        D={}
        global max_level
        max_level = 0
        def fun(root, level):
            global max_level
            if root == None:
                return None
            D[level] = root.val
            max_level = max(max_level, level)
            fun(root.left, level + 1)
            fun(root.right, level + 1)
            return
        
        fun(root, 0)
        return [D[level] for level in range(0, max_level+1)]
        