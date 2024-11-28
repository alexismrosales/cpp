class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        n, m = len(haystack), len(needle)
        if m > n:
            return -1
        for p1 in range(n - m + 1):
            if haystack[p1 : p1 + m] == needle:
                return p1
        return -1


# ? like wtf
class SolutionGPT:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        return haystack.find(needle)
