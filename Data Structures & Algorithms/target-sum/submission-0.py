class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        # base case is we can create 0 1-way before using any nums
        dp[0] = 1

        for n in nums:
            dp2 = defaultdict(int)
            for d in dp:
                dp2[d + n] += dp[d]
                dp2[d - n] += dp[d]
            dp = dp2
        
        return dp[target]