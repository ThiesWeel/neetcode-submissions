# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # first we define the condition
        # if node.val < max_val_seen, I think bfs makes sense here, with an extra arg, which is max seen
        self.good_count = 0
        if not root:
            return 0 
        def bfs(curr, max_seen = float('-inf')):

            
            if curr.val >= max_seen:
                # new max_seen, but we will just use max(max_seen, curr.val) for recusive call
                # but here we can add one to good_count
                self.good_count += 1

            if curr.left:
                bfs(curr.left, max_seen = max(max_seen, curr.val))
            if curr.right:
                bfs(curr.right, max_seen = max(max_seen, curr.val))
        bfs(root)
        return self.good_count