from typing import List


class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        min_val, max_value = min(nums), max(nums)  # min 0, max 2
        # [1 0 3]
        #  0 1 2
        # 2 - 0 + 1 = 3
        freqs = [0] * (max_value - min_val + 1)  # 0 1 2

        for num in nums:
            # 2 - 1 = 1 # 1 - 1 = 0
            freqs[num - min_val] += 1

        index = 0
        for i in range(0, len(freqs)):
            while freqs[i] > 0:
                nums[index] = i + min_val
                index += 1
                freqs[i] -= 1
