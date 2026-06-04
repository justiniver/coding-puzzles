class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        ans = nums[0]

        for x in nums[1:]:
            cand1 = x
            cand2 = x * currMax
            cand3 = x * currMin

            currMax = max(cand1, cand2, cand3)
            currMin = min(cand1, cand2, cand3)

            ans = max(ans, currMax)

        return ans