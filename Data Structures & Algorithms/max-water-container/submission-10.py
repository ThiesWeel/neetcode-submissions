class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_water = 0


        left = 0
        right = n - 1
        
        
        # to update, choose the pointer that would move to the highest value
        while left != right:
            water = (right - left)*min(heights[left],heights[right])
            print(water)
            # update max water volume
            max_water = max(water, max_water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1


        return max_water