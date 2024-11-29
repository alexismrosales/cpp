# Problem: Just works if the right barrier is bigger thant the left one
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1 = 0
        p2 = 0
        trappedWater = 0
        nothing = False
        while p2 < len(height) - 1:
            # Ignoring empty spaces at the beggining
            if p1 == 0 and height[p1] == 0:
                print("entre1")
                nothing = True
                p1 += 1
                p2 = p1
                continue
            # Ignoring empty spaces
            if nothing and height[p1] == 0:
                p1 += 1
                p2 = p1
                continue

            p2 += 1
            if height[p1] > height[p2]:
                trappedWater += height[p1] - height[p2]
                continue

            # In case we reach a place were cant be more water
            p1 = p2

        return trappedWater
