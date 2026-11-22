# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we need to visit every node to be sure which are the most right leaves from the tree
        # using dfs is easier then bfs as the comparison can happen at each level, no extra storage
        # required for a keeping track of the most right node at each depth
        if not root:
            return []
        
        queue = deque([root])
        res = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()       # Always take from the FRONT of the line
                
                if i == level_size - 1:      # Is this the LAST person from this level?
                    res.append(node.val)     # If yes, they are the rightmost node!
                    
                if node.left:
                    queue.append(node.left)  # New kids always go to the BACK of the line
                if node.right:
                    queue.append(node.right)
        return res

            