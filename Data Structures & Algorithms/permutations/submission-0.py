class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        n = len(nums)
        def dfs(i):
            if i == n:
                out.append(nums.copy())
                return
    
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)
                nums[j], nums[i] = nums[i], nums[j]
        
        dfs(0)
        return out