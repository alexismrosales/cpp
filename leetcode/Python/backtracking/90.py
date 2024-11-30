class Solution(object):
    def subsetsWithDup(self, nums):
        subsets = []
        nums.sort()

        def backtracking(index, sett):
            # Add set
            subsets.append(sett[:])
            for i in range(index, len(nums)):
                # Avoid duplicates
                if i > index and nums[i] == nums[i - 1]:
                    continue
                # Add actual number and start recursion
                sett.append(nums[i])
                backtracking(index + 1, sett)
                sett.pop()  # Backtrack

        backtracking(0, [])
        return subsets
