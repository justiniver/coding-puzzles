class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if (board[r][c] == 'O'):
                    connected = set()
                    enclosed = True
                    stack = [(r, c)]
                    while stack:
                        curr_r, curr_c = stack.pop()
                        connected.add((curr_r, curr_c))
                        if (curr_r in (0, m - 1) or
                            curr_c in (0, n - 1)):
                            enclosed = False
                        for dr, dc in dirs:
                            nr, nc = curr_r + dr, curr_c + dc
                            if (0 <= nr < m and
                                0 <= nc < n and
                                (nr, nc) not in connected and
                                board[nr][nc] == 'O'):
                                stack.append([nr, nc])
                    if enclosed:
                        for xr, xc in connected:
                            board[xr][xc] = 'X'