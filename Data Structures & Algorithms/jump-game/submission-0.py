class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currIdx = len(nums) - 1

        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= currIdx:
                currIdx = i

        return currIdx == 0