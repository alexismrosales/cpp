from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = []
        totalValue = 1
        zeroes = 0
        for n in nums:
            if n != 0:
                totalValue *= n
            else: 
                zeroes += 1
        # In case all arrays are zero
        if zeroes > 1:
            return [0] * len(nums)

        # Managing cases with one zero
        for n in nums:
            if n != 0 and zeroes > 0:
                solution.append(0)
            elif n == 0 and zeroes > 0:
                solution.append(totalValue)
        if zeroes > 0:
            return solution
        for n in nums:
            solution.append(totalValue/n)
        return solution
        
