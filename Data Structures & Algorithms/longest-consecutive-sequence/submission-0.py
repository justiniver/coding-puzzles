class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 1
        for i in range(len(nums)):
            if nums[i] - 1 in set(nums):
                continue
            else:
                currNum = nums[i]
                currLen = 1
                while (currNum + 1 in set(nums)):
                    currNum += 1
                    currLen += 1
                maxLen = max(maxLen, currLen)

        return maxLen
        