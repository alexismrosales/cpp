from collections import defaultdict


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        numbersvisited = defaultdict(int)  # { number : position}
        for i, num in enumerate(nums):
            if num in numbersvisited:
                if i - numbersvisited[num] <= k:
                    return True
            numbersvisited[num] = i

        return False
