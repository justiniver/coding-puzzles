class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        maxProd = nums[0]
        for i in range(1, len(nums)):
            cand1 = nums[i]
            cand2 = nums[i] * dp[i - 1][0]
            cand3 = nums[i] * dp[i - 1][1]
            dp[i][0] = max(cand1, cand2, cand3)
            dp[i][1] = min(cand1, cand2, cand3)
            maxProd = max(maxProd, dp[i][0])

        return maxProd