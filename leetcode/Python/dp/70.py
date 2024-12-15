class Solution:
    def climbStairs(self, n: int) -> int:

        return self.dp(n, {})

    def dp(self, n: int, memo: dict) -> int:
        if n <= 1:
            return 1
        if n not in memo:
            memo[n] = self.dp(n - 1, memo) + self.dp(n - 2, memo)
        return memo[n]
