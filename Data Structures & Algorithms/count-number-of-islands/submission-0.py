class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(r, c):
            q = deque([(r, c)])
            visit.add((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        (nr, nc) not in visit and
                        grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        visit.add((nr, nc))

        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    num_islands += 1