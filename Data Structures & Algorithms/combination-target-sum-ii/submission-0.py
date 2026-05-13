class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out = []
        comb = []

        def create_curr_target_from_i(curr_target: int, i: int):
            if curr_target == 0:
                out.append(comb.copy())
                return
            if curr_target < 0 or i >= len(candidates):
                return
            
            curr = candidates[i]
            if curr > curr_target:
                return

            comb.append(curr)
            create_curr_target_from_i(curr_target - curr, i + 1)
            comb.pop()

            while i < len(candidates) and candidates[i] == curr:
                i += 1
            create_curr_target_from_i(curr_target, i)

        create_curr_target_from_i(target, 0)
        return out
