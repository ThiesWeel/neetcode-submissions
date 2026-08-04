from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []          # stack of indices
        max_area = 0

        # add sentinel to flush stack at the end
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                mid = stack.pop()
                height = heights[mid]

                # left boundary
                left = stack[-1] if stack else -1
                # right boundary is current index i
                width = i - left - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
