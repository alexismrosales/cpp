from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        currentSum = sum(nums[left:right])
        maxAverage = currentSum/k
        while right < len(nums):
            currentSum -= nums[left]
            currentSum += nums[right]
            right+=1
            left+=1
            maxAverage = max(maxAverage, currentSum/k)
        return maxAverage
        
