from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def backtracking(currentList):
            # Base case
            if len(currentList) == len(nums):
                permutations.append(currentList[:])
                return
            # For every number
            for n in nums:
                if n not in currentList:
                    currentList.append(n)
                    backtracking(currentList)
                    currentList.pop()

        backtracking([])
        return permutations

