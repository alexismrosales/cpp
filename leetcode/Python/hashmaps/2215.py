from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Set = set(nums1) 
        nums2Set = set(nums2)
        return [ list(nums1Set.difference(nums2Set)),list(nums2Set.difference(nums1Set))]

class Solution2:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Dict = {}
        nums2Dict = {}
        for num in nums1:
            nums1Dict[num] = 0
        for num in nums2:
            nums2Dict[num] = 0
        ans1 = []
        ans2 = []
        for n in nums1:
            if n not in nums2Dict:
                if n not in ans1:
                 ans1.append(n)
        for n in nums2:
            if n not in nums1Dict:
                if n not in ans2:
                    ans2.append(n)
        return [ans1, ans2]
                


