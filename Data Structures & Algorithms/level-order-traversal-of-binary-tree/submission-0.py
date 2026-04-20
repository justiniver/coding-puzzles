# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        out = []
        level = []
        q = deque([(root, 0)])
        depth = 0

        while q:
            currNode, currDepth = q.popleft()
            if currDepth == depth:
                level.append(currNode.val)
            else:
                out.append(level)
                level = [currNode.val] # reset level
                depth = currDepth

            if currNode.left:
                q.append((currNode.left, currDepth + 1))
            if currNode.right:
                q.append((currNode.right, currDepth + 1))

        out.append(level)     