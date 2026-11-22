# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs, recursive calling, with a counter inside each recursive call
        res = []
        def bfs(curr, nest_count = 0):
            # curr could be None node, then we do not add an empty list
            # nor do append val to res
            if not curr:
                return
            while len(res) <= nest_count:
                res.append([])
            res[nest_count].append(curr.val)

            bfs(curr.left, nest_count = nest_count + 1)
            bfs(curr.right, nest_count = nest_count + 1)
            
        bfs(root)
        return res