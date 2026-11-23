class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for O(1) lookup
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left: int, right: int) -> Optional[TreeNode]:
            # Base case: no elements to construct the subtree
            if left > right:
                return None

            # 1. Pick the current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # 2. Find where this root splits the inorder array
            mid = inorder_map[root_val]

            # 3. Build left subtree first (because preorder visits Root -> Left -> Right)
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)
