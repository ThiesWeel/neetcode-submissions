# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. Both nodes are empty -> they match at this branch
        if not p and not q:
            return True
        
        # 2. Only one is empty, or their values differ -> mismatch!
        if not p or not q or p.val != q.val:
            return False
            
        # 3. Both left subtrees AND both right subtrees must match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
