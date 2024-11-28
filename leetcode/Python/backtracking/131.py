class Solution(object):
    def partition(self, s):
        solutions = []
        solution = []

        def backtracking(start):
            if start == len(s):
                # deep copy
                solutions.append(solution[:])
                return
            for i in range(start, len(s)):
                substr = s[start : i + 1]
                if self.isPalindrome(substr):
                    solution.append(substr)
                    backtracking(i + 1)
                    solution.pop()

        backtracking(0)
        return solutions

    def isPalindrome(self, s):
        return s == s[::-1]
