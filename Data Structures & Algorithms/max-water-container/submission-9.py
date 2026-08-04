class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Using pointers, we either bring left or right to middle
        # We always have to search all bins, untill left >= right
        n = len (heights) - 1
        left = 0 
        right = n
        max_v = 0
        while left <= right:
            h_l = heights[left]
            h_r = heights[right]
            distance = right - left 
            if h_l <= h_r:
                v = h_l*distance
                if v > max_v:
                    max_v = v
                left +=1
            elif h_l > h_r:
                v = h_r*distance
                if v > max_v:
                    max_v = v
                right -= 1
        return max_v

            