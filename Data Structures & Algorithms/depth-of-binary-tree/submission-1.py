# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def recursive(node, path):
            if node.left:
                left_path = recursive(node.left, path + 1)
            else:
                left_path = path

            if node.right:
                right_path = recursive(node.right, path + 1)
            else:
                right_path = path

            return max(left_path, right_path)

        return recursive(root, 1)


        