from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        def backtracking(currentList, startIndex):
            allSubsets.append(currentList[:])
            i = startIndex
            while i < len(nums):
                currentList.append(nums[i])
                backtracking(currentList, i + 1)
                currentList.pop()
                i+=1
        backtracking([], 0)
        return allSubsets


        
