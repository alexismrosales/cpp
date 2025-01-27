from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum = 0
        maxAltitude = 0
        for g in gain:
            sum += g
            maxAltitude = max(maxAltitude, sum)
        return maxAltitude


