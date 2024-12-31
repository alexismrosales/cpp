from typing import List
# [1,1,1,0,0,0,1,1,1,1,0]
#            ^
#           currentSub = 3 -> currentSub = 0

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        currentZeroes = 0
        longest = 0
        for right in range(0, len(nums)): 
                if nums[right] == 0:
                    currentZeroes +=1
                while currentZeroes > k:
                    if nums[left] == 0:
                        currentZeroes -= 1
                    left += 1
                longest = max(longest,right - left +1)
        return longest


