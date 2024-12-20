from typing import List


"""""
max = -11
current = 1
[2,3,-2,4]
 ^
current *= num -> current = 2
max = current
[2,3,-2,4]
      ^
current *= num -> current = 6
max = current // max = 6
[2,3,-2,4]
      ^
current *= num -> current = -12
max // max = 6
[2,3,-2,4]
        ^
current *= num -> current = -48
max // max = 6
and then start from the the end
"""""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current = 1
        maxValue = max(nums)

        for i in range(len(nums)):
            current *= nums[i]
            maxValue = max(maxValue, current)
            if current == 0:
                current = 1
        i = len(nums)-1
        current = 1
        while i >= 0:
            current *= nums[i]
            maxValue = max(maxValue, current)
            if current == 0:
                current = 1
            i-=1
        return maxValue
