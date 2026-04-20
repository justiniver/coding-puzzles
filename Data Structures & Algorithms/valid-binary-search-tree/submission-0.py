# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, vmin, vmax = stack.pop()
            if not node:
                continue
            if not (vmin < node.val < vmax):
                return False
            stack.append((node.left, vmin, node.val))
            stack.append((node.right, node.val, vmax))

        return True