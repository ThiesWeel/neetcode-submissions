class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # 1) find row
        top, bot = 0, rows - 1
        row = -1
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
                row = mid
                break
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                top = mid + 1

        if row == -1:
            return False

        # 2) binary search in row
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
