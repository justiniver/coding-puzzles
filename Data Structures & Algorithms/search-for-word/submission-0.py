class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(m):
            for c in range(n):
                if board[r][c] != word[0]:
                    continue
                stack = [(r, c, {(r, c)}, 1)]
                while stack:
                    cur_r, cur_c, path, w_i = stack.pop()
                    if w_i == len(word):
                        return True
                    for dr, dc in dirs:
                        nr, nc = cur_r + dr, cur_c + dc
                        if (0 <= nr < m and
                            0 <= nc < n and
                            board[nr][nc] == word[w_i] and
                            (nr, nc) not in path):
                            stack.append((nr, nc, path | {(nr, nc)}, w_i + 1))

        return False
