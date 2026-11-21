# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.pl = []
        self.ql = []
        def dfs(curr,isp):
            if not curr:
                # curr node = None, 
                if isp:
                    self.pl.append(None)
                else:
                    self.ql.append(None)
                return None

            if isp:
                self.pl.append(curr.val)
            else:
                self.ql.append(curr.val)

            lc = dfs(curr.left,isp)
            rc = dfs(curr.right,isp)
            
        dfs(p,True)
        dfs(q, False)
        return self.pl == self.ql