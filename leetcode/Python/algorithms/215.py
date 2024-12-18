from math import pi
from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()

        def partition(nums, start, end):
            random_pivoting = random.randint(start, end)
            swap(nums, end, random_pivoting)  # Move random pivot to the end

            pivot = nums[end]  # Use the last element as the pivot
            i = start

            # Modify comparison for descending order
            for j in range(start, end):
                if nums[j] >= pivot:  # Greater instead of less
                    swap(nums, i, j)
                    i += 1

            swap(nums, i, end)  # Move pivot to the correct position
            return i

        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        start, end = 0, len(nums) - 1
        k = k - 1
        while start <= end:
            pivot_index = partition(nums, start, end)
            if pivot_index == k:
                return nums[pivot_index]
            elif pivot_index < k:
                start = pivot_index + 1
            else:
                end = pivot_index - 1
        return 0
