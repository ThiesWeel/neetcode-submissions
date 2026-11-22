# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([root]) 
        if not root:
            return []
        while queue:
            
            current_level = []
            for _ in range(len(queue)):
                # pop node from queue
                node = queue.popleft()
                # Enqueue children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # append value to current level
                current_level.append(node.val)
            
            res.append(current_level)

        return res
            
       
       
       
'''
# dfs, recursive calling, with a counter inside each recursive call
res = []
def dfs(curr, nest_count = 0):
    # curr could be None node, then we do not add an empty list
    # nor do append val to res
    if not curr:
        return
    while len(res) <= nest_count:
        res.append([])
    res[nest_count].append(curr.val)

    bfs(curr.left, nest_count = nest_count + 1)
    bfs(curr.right, nest_count = nest_count + 1)
    
dfs(root)
return res
'''