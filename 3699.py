class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = (10 ** 9) + 7
        mid = r - l + 1
        dp = [1] * mid

        for i in range(2, n + 1):
            dp.reverse()
            s = 0
            for j in range(mid):
                dp[j], s = s, (s + dp[j]) % MOD

        return (sum(dp) % MOD << 1) % MOD