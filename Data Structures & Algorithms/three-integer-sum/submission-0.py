class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        used_1 = set()

        for i in range(len(nums)):
            if nums[i] in used_1:
                continue
            used_1.add(nums[i])

            seen = set()
            for j in range(len(nums)):
                if i == j:
                    continue

                need = -(nums[i] + nums[j])
                if need in seen:
                    out.add(tuple(sorted((nums[i], nums[j], need))))

                seen.add(nums[j])

        return [list(triplet) for triplet in out]