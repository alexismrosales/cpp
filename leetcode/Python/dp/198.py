from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
            def find_maximum(i: int, currentVisitedHouses) ->int:
                # In case there is a visited house
                if i in currentVisitedHouses: 
                    return currentVisitedHouses[i]
                if i >= len(nums):
                    return 0
                if i == len(nums)-1:
                    return nums[i]
                currentVisitedHouses[i] = max(find_maximum(i+1, currentVisitedHouses), find_maximum(i+2, currentVisitedHouses) + nums[i])
                return currentVisitedHouses[i]
            find_maximum(0, {})
            return 0
