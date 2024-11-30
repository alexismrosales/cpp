class Solution(object):
    def subsets(self, nums):
        subs = []

        def bactracking(index, sett):
            subs.append(sett[:])
            for i in range(index, len(nums)):
                sett.append(nums[i])
                bactracking(i + 1, sett)
                sett.pop()

        bactracking(0, [])
        return subs
