# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # for each node check that curr.left.val < curr.val < curr.right.val
        # if curr.l/r of course
        # dfs resursive call
        self.bst = True
        if not root:
            return self.bst

        
        def dfs(curr, mi = -float('inf'), ma = float('inf')):
            if not self.bst:
                # we already concluded the tree aint a bst
                pass
            if not (mi < curr.val < ma):
                self.bst =  False
                
            # for left leaf, must be smaller than curr, 
            if curr.left and mi < curr.left.val < ma:
                dfs(curr.left, mi = mi, ma = min(curr.val, ma))

            elif curr.left:
                self.bst = False    
                pass

            # for right leaf, must be smaller than curr, 
            if curr.right and mi < curr.right.val < ma:
                dfs(curr.right, mi = max(mi, curr.val), ma = ma)

            elif curr.right:
                self.bst = False    
                pass
                

        dfs(root)
        return self.bst
