class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        subsets = []
        def dfs(i):
            if i >= len(nums):
                out.append(subsets.copy())
                return

            subsets.append(nums[i])
            dfs(i + 1)

            subsets.pop()
            dfs(i + 1)
        
        dfs(0)
        return out