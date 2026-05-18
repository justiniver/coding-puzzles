class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(m):
            for c in range(n):
                if (r, c) in visited or grid[r][c] == 0:
                    continue
                stack = [(r, c)]
                curr_area = 0
                while stack:
                    curr_r, curr_c = stack.pop()
                    if (curr_r, curr_c) in visited:
                        continue
                    visited.add((curr_r, curr_c))
                    for x, y in dirs:
                        nr, nc = curr_r + x, curr_c + y
                        if (0 <= nr < m and
                            0 <= nc < n and
                            grid[nr][nc] == 1 and
                            (nr, nc) not in visited):
                            stack.append((nr, nc))
                    curr_area += 1
                max_area = max(max_area, curr_area)
        
        return max_area