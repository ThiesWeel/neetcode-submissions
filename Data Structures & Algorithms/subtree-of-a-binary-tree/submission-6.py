# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.subTreeFound = False
        def subTreeComp(curr, scurr):
            if not curr and not scurr:
                return True

            if not curr or not scurr or curr.val != scurr.val:
                return False
            
            return subTreeComp(curr.left, scurr.left) and subTreeComp(curr.right, scurr.right)

        def dfs(curr):
            if not curr:
                return None
            
            if curr.val == subRoot.val:
                # possible subtree
                if self.subTreeFound:
                    return None
                else:
                    self.subTreeFound = subTreeComp(curr,subRoot)
            dfs(curr.left)
            dfs(curr.right)
            return None

        if not subRoot: 
            return True
        

        dfs(root)
        return self.subTreeFound
            