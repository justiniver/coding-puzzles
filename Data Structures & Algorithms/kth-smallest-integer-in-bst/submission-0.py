# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [(root, False)]
        nth = 0
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if not visited:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
            else:
                nth += 1
                if nth == k:
                    return node.val
                    
        return 0