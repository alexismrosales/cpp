from collections import defaultdict


class Solution(object):
    def removeDuplicates(self, nums):
        numbers = defaultdict(int)
        for num in nums:
            numbers[num] += 1
        i = 0
        while i < len(nums):
            if numbers[nums[i]] > 2:
                numbers[nums[i]] -= 1
                del nums[i]  # deleting leaving size of nums len(nums) = len(nums) - 1
            else:
                i += 1  # if num is not repeated i advance
