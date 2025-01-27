from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ocurrences = {}
        timesSet = set()
        for n in arr:
            if n in ocurrences:
                ocurrences[n] += 1
            else:
                ocurrences[n] = 1

        for oc in ocurrences.values():
            if oc in timesSet:
                return False
            else:
                timesSet.add(oc)
        return True

        
