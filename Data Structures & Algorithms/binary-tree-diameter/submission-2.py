# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0 
        if not root:
            return 0

        def recursive(node):
            if not node:
                return 0
            left_height = recursive(node.left)
            right_height = recursive(node.right)

            # Add left_height + right_height instead of separating with a comma
            self.max_dia = max(self.max_dia, left_height + right_height)
            return 1 + max(left_height, right_height)

        recursive(root)
        return self.max_dia