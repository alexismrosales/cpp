from typing import List


class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.binarySearch(row, target):
                return True
        return False

    def binarySearch(self, row: List[int], target: int) -> bool:
        start = 0
        end = len(row) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False


class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] < target and matrix[mid][-1] > target:
                break
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1
        row = (top + bottom) // 2
        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
