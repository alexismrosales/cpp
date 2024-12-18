from math import pi
from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def merge_sort(nums, left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort(nums, left , mid)
                merge_sort(nums, mid + 1, right)
                merge(nums, left, mid, right)

        def merge(nums, left, mid, right):
            # Size of arrays to subarray
            # is mid - left because is needed the range from start to mid
            n1 = mid - left + 1
            n2 = right - mid

            # Creating arrays
            L = [0] * n1
            R = [0] * n2

            # Saving numbers in temporal arrays
            for i in range(n1):
                L[i] = nums[left + i]
            for j in range(n2):
                R[j] = nums[mid + 1 + j]

            i = 0 # Initial index of first subarray
            j = 0 # Initial index of second subarray
            k = left #Initial index of merged subarray

            # Merge temp arrays into the original one but in order
            while i < n1 and j < n2:
                if L[i] >= R[j]: # If L[i] val is smaller is save in the array else R[j]
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1
            
            # In case there are remaining elements on left or right array just add the rest
            while i < n1:
                nums[k] = L[i]
                i+=1
                k+=1
            while j < n2:
                nums[k] = R[j]
                j+=1
                k+=1
        merge_sort(nums, 0, len(nums)-1)
        return nums[k-1]
