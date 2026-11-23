class Solution:
    def isValidBST(self, root: Optional[TreeNode], mi: float = float('-inf'), ma: float = float('inf')) -> bool:
        if not root:
            return True
        
        if not (mi < root.val < ma):
            return False
        
        return (self.isValidBST(root.left, mi, root.val) and 
                self.isValidBST(root.right, root.val, ma))