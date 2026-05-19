class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        safe = set()
        border = (
            [(0, c) for c in range(n)] +
            [(m - 1, c) for c in range(n)] +
            [(r, 0) for r in range(m)] +
            [(r, n - 1) for r in range(m)]
        )

        for r, c in border:
            if ((r, c) not in safe and
                board[r][c] == 'O'):
                stack = [(r, c)]
                while stack:
                    curr_r, curr_c = stack.pop()
                    safe.add((curr_r, curr_c))
                    for dr, dc in dirs:
                        nr, nc = curr_r + dr, curr_c + dc
                        if (0 <= nr < m and
                            0 <= nc < n and
                            (nr, nc) not in safe and
                            board[nr][nc] == 'O'):
                            stack.append((nr, nc))
        
        for r in range(m):
            for c in range(n):
                if (board[r][c] == 'O' and
                    (r, c) not in safe):
                    board[r][c] = 'X'