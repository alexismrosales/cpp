"""""
NOT MY SOLUTION
"""""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        output = 0
        # index, element
        for right, c in enumerate(s):
            if c in seen:
                left = max(left, seen[c] + 1)
            output = max(output, right - left + 1)
            seen[c] = right
        return output
