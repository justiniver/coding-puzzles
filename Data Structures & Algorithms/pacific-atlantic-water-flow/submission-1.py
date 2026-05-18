class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacifics = [(r, 0) for r in range(m)] + [(0, c) for c in range(n)]
        atlantics = [(r, n - 1) for r in range(m)] + [(m - 1, c) for c in range(n)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(beach: list) -> set:
            visited = set()
            for r, c in beach:
                if (r, c) in visited:
                    continue
                stack = [(r, c)]
                while stack:
                    curr_r, curr_c = stack.pop()
                    visited.add((curr_r, curr_c))
                    for dr, dc in dirs:
                        nr, nc = curr_r + dr, curr_c + dc
                        if (0 <= nr < m and
                            0 <= nc < n and
                            (nr, nc) not in visited and
                            heights[nr][nc] >= heights[curr_r][curr_c]):
                            stack.append((nr, nc))
            return visited

        pacific_set = dfs(pacifics)
        atlantic_set = dfs(atlantics)
        return list(pacific_set & atlantic_set)