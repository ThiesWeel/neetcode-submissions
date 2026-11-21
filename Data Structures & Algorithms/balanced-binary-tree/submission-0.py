# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(curr):
            if not curr:
                return 0
            
            hl = dfs(curr.left)
            hr = dfs(curr.right)

            if abs(hr-hl) > 1:
                self.balanced = False
            return 1+max(hl,hr)
        dfs(root)
        return self.balanced
                