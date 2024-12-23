from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        self.mergeSort_algorithm(nums)
        i = 1
        maxGap = -1
        while i < len(nums):
            maxGap = max(nums[i] - nums[i - 1], maxGap)
            i += 1
        return maxGap
    def mergeSort_algorithm(self,arr):
        def mergeSort(arr, left, right):
            if left < right:
                mid = (left + right) // 2
                mergeSort(arr, left, mid)
                mergeSort(arr, mid + 1, right)
                merge(arr, left,mid,right)

        def merge(arr, left, mid, right):
            n1 =  mid - left + 1
            n2 =  right - mid

            L = [0] * n1
            R = [0] * n2

            for i in range(n1):
                L[i] = arr[left + i]
            for j in range(n2):
                R[j] = arr[mid + j + 1]

            i, j, k = 0, 0, left

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k += 1

            while i < n1:
                arr[k] = L[i]
                i+=1
                k+=1
            while j < n2:
                arr[k] = R[j]
                j+=1
                k+=1
        mergeSort(arr, 0, len(arr)-1)
