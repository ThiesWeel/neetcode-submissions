class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(node):
            if not node:
                return 0
            
            # Get the height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update the largest diameter found so far (number of edges)
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return this node's height to its parent
            return 1 + max(left_height, right_height)

        height(root)
        return self.max_diameter
