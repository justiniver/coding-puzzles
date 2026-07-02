class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        max_map = dict()
        for i, c in enumerate(s):
            max_map[c] = i

        out = []
        grp_size = 0
        last = 0
        for i, c in enumerate(s):
            grp_size += 1
            last = max(last, max_map[c])
            if i == last:
                out.append(grp_size)
                grp_size = 0
        
        return out