class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0 # takes 0 coins to make 0
        for c in coins:
            for i in range(c, amount + 1):
                if dp[i - c] >= 0:
                    if dp[i] == -1:
                        dp[i] = dp[i - c] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - c] + 1)
        
        return dp[-1]