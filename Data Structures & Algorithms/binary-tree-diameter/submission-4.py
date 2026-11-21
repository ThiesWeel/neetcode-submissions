# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0
        def dfs(curr):
            if not curr:
                return 0
            hl = dfs(curr.left)
            hr = dfs(curr.right)

            self.max_dia = max(self.max_dia, hl+hr)
            return 1 + max(hl,hr)
        dfs(root)
        return self.max_dia