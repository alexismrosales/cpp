from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        nums.sort()

        def backtracking(current: List[int]):
            if len(current) == len(nums):
                result.append(current[:])
                return

            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                used[i] = True
                current.append(nums[i])
                backtracking(current)
                current.pop()
                used[i] = False

        backtracking([])
        return result
