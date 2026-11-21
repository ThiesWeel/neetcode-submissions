class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_dia = 0
        # Stores the computed height of each processed node
        heights = {None: 0}
        # Stack holds tuples of (node, children_already_visited)
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if visited:
                # Both children have already been processed and stored in `heights`
                left_height = heights[node.left]
                right_height = heights[node.right]

                max_dia = max(max_dia, left_height + right_height)
                heights[node] = 1 + max(left_height, right_height)
            else:
                # Push node back as True so it processes AFTER its children (post-order)
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return max_dia
