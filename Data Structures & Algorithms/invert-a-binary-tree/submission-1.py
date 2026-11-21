class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def recursive(node):
            if not node:
                return
            
            # Swap the children
            node.left, node.right = node.right, node.left
            
            # Recurse on both children
            recursive(node.left)
            recursive(node.right)

        recursive(root)
        return root
