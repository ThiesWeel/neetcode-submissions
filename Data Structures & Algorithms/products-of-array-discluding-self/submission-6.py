class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # 1. Build the left products directly in our output array
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
            
        # 2. Use a single variable to keep track of the right products
        right_product = 1
        
        # 3. Walk backwards, multiplying the left product by the running right product
        for i in range(n - 1, -1, -1):
            res[i] *= right_product      # Multiply by everything to the right
            right_product *= nums[i]     # Update the right product for the next step
            
        return res