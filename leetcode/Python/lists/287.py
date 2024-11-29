from collections import defaultdict


class Solution(object):
    def findDuplicate(self, nums):
        duplicated = defaultdict(int)
        for num in nums:
            duplicated[num] += 1
            if duplicated[num] > 1:
                return num


# Using Floyd's Algorithm, ONLY WORKS IF THERE IS ONLY ONE NUMBER DUPLICATED
class OtherSolution(object):
    def findDuplicate(self, nums):
        t = nums[0]
        h = nums[0]
        # if there are two duplicates cycle stop
        while True:
            t = nums[t]
            h = nums[nums[h]]
            if t == h:
                break
        # after detecting the cycle, t start from the beginning and search after finding a coincidence
        t = nums[0]
        while t != h:
            t = nums[t]
            h = nums[h]
        return t
