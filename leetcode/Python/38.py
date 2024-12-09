class Solution:
    def countAndSay(self, n: int) -> str:
        actualStr = "1"
        if n == 1:
            return actualStr
        for _ in range(0, n - 1):
            actualStr = self.rle(actualStr)
        return actualStr

    def rle(self, s: str) -> str:
        compressed_number = ""
        times = 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                compressed_number += str(times)
                compressed_number += s[i - 1]
                times = 1
            else:
                times += 1
        compressed_number += str(times)
        compressed_number += s[-1]
        return compressed_number
