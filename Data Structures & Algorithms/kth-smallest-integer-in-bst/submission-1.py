class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None

        def dfs(curr):
            # Base case: stop if we hit a dead end or already found the answer
            if not curr or self.result is not None:
                return
            
            # 1. Go all the way left first (smaller values)
            dfs(curr.left)
            
            # 2. Process current node
            self.count += 1
            if self.count == k:
                self.result = curr.val
                return
            
            # 3. Explore right subtree (larger values)
            dfs(curr.right)

        dfs(root)
        return self.result