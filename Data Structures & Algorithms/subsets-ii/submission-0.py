class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        comb = []
        def create_comb_from_i(i: int):
            if i >= len(nums):
                out.append(comb.copy())
                return
            
            curr = nums[i]
            comb.append(curr)
            create_comb_from_i(i + 1)
            comb.pop()

            while i + 1 < len(nums) and nums[i + 1] == curr:
                i += 1
            create_comb_from_i(i + 1)
        
        create_comb_from_i(0)
        return out