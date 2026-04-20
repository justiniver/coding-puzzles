# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        stack = [(root, root.val)]
        while stack:
            X, path_max = stack.pop()
            if not X:
                continue
            if X.val >= path_max:
                good += 1
                path_max = X.val
            stack.extend([(X.left, path_max), (X.right, path_max)])

        return good