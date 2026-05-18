class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # a correct but non-optimal solution. Need to flip logic and start from the ocean
        m, n = len(heights), len(heights[0])
        pacific_set = {(r, 0) for r in range(m)} | {(0, c) for c in range(n)}
        atlantic_set = {(r, n - 1) for r in range(m)} | {(m - 1, c) for c in range(n)}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(m):
            for c in range(n):
                if (r, c) in pacific_set and (r, c) in atlantic_set:
                    continue
                stack = [(r, c, r, c)]
                visited = set()
                while stack:
                    curr_r, curr_c, orig_r, orig_c = stack.pop()
                    curr = (curr_r, curr_c)
                    orig = (orig_r, orig_c)
                    if curr in visited:
                        continue
                    if curr in pacific_set:
                        pacific_set.add(orig)
                    if curr in atlantic_set:
                        atlantic_set.add(orig)
                    if orig in pacific_set and orig in atlantic_set:
                        break
                    visited.add((curr_r, curr_c))
                    for dr, dc in dirs:
                        nr, nc = curr_r + dr, curr_c + dc
                        if (0 <= nr < m and
                            0 <= nc < n and
                            (nr, nc) not in visited and
                            heights[nr][nc] <= heights[curr_r][curr_c]):
                            stack.append((nr, nc, orig_r, orig_c))
        
        return list(pacific_set & atlantic_set)