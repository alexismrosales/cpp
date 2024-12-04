from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        i = 0
        start_rotation = -1
        # finding where the list start
        while i < len(nums) - 1:
            if nums[i] > nums[i + 1]:
                start_rotation = i + 1
            i += 1

        # if start_rotation is -1 it means, the list is not rotated
        if start_rotation == -1:
            return self.binary_search(nums, 0, len(nums) - 1, target)
        # if the number is less than num it means is in the other part
        elif target < nums[0]:
            return self.binary_search(
                nums,
                start_rotation,
                len(nums) - 1,
                target,
            )
        else:
            return self.binary_search(
                nums,
                0,
                start_rotation - 1,
                target,
            )

    def binary_search(self, nums: List[int], start: int, end: int, target: int) -> int:
        while start <= end:
            mid = start + (end - start) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            # search in right side
            elif nums[mid] < target:
                start = mid + 1
            # search in left side
            else:
                end = mid - 1
        return -1
