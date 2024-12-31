# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        mid = 0
        while start <= end:
            mid = (start +end) // 2
            # n belongs to R, where n is an integer. 
            # n > 0 or n < 0 or n == 0
            result = guess(mid)
            if result == 0:
                break
            elif result == -1:
                end = mid - 1
            else:
                start = mid + 1
        return mid
