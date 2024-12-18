# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(version: int) -> bool:
    return True

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def search():
            start = 0
            end = n-1
            while start <= end:
                mid = start + (end - start) // 2
                # if there is a bad version check in the left side
                checkVersion = isBadVersion(mid + 1)
                if checkVersion:
                    end = mid - 1
                else:
                    start = mid + 1
            return start+1
        return search()
