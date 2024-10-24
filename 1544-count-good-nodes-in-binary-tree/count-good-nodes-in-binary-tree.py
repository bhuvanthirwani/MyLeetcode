# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def inorder(node, _max):
            nonlocal count
            if not node:
                return
            if node.val >= _max:
                count += 1
            _max = max(_max, node.val)
            inorder(node.left, _max)
            inorder(node.right, _max)
            return
        inorder(root, -9999999999)
        return count