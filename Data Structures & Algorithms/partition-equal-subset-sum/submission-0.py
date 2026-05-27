from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2 == 1:
            return False

        @cache
        def build_sums_from_i(i: int, curr_sum: int) -> bool:
            if curr_sum == target:
                return True
            if curr_sum > target:
                return False
            if i >= len(nums):
                return False
            
            curr_sum += nums[i]
            if build_sums_from_i(i + 1, curr_sum):
                return True
            curr_sum -= nums[i]
            if build_sums_from_i(i + 1, curr_sum):
                return True

            return False

        return build_sums_from_i(0, 0)