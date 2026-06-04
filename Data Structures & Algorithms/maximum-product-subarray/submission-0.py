class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        maxProd = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(nums[i], nums[i] * dp[i - 1][0], nums[i] * dp[i - 1][1])
            dp[i][1] = min(nums[i], nums[i] * dp[i - 1][0], nums[i] * dp[i - 1][1])
            maxProd = max(maxProd, dp[i][0])

        return maxProd