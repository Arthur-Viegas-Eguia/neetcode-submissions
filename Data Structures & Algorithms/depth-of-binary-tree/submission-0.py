# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def maxDepthHelper(root):
            if not root:
                return 0
            depth = 1 + max(maxDepthHelper(root.left), maxDepthHelper(root.right))
            return depth
        return maxDepthHelper(root)