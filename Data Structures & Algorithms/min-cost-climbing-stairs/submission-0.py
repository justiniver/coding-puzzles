class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float('inf')] * (len(cost) + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost) + 1):
            addCurr = cost[i] if i != len(cost) else 0
            dp[i] = min(dp[i - 2], dp[i - 1]) + addCurr

        return dp[-1]