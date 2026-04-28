class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        curr_sum = 0
        subset = []
        n = len(nums)
        def dfs(i):
            nonlocal curr_sum
            if i >= n or curr_sum > target:
                if curr_sum == target and subset:
                    out.append(subset.copy())
                return
            add = nums[i]
            subset.append(add)
            curr_sum += add
            dfs(i)

            sub = subset.pop()
            curr_sum -= sub
            dfs(i + 1)

        dfs(0)
        return out