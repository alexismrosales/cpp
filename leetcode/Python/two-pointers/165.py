class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        # In case the main number is different > or <
        if v1[0] < v2[0]:
            return -1
        elif v1[0] > v2[0]:
            return 1
        i = self.jumpZeroes(v1[1])
        j = self.jumpZeroes(v2[1])
        print(i, j)
        return 0

    def jumpZeroes(self, number:str)-> int:
        # In case there are no zeroes at the left
        if number[0] != 0:
            return 0
        i = 0
        while i < len(number):
            if number[i] != 0:
                return i
            i+=1
        return -1
