# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, 0)]
        seen_depths = set()
        out = []
        while stack:
            curr, depth = stack.pop()
            if not curr:
                continue
            if depth not in seen_depths:
                out.append(curr.val)
                seen_depths.add(depth)
            stack.append((curr.left, depth + 1))
            stack.append((curr.right, depth + 1))
        
        return out
        