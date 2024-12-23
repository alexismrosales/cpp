class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n:int, steps: dict) -> int:
            if n in steps:
                return steps[n]
            if n <= 1:
                return 1
            # Need to do 1 or 2 steps
            steps[n] = dp(n-1, steps) + dp(n-2, steps)
            return steps[n]
        return dp(n, {})

