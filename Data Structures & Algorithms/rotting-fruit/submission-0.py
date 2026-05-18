class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = set()
        visit = set()
        rotten = []

        for i, r in enumerate(grid):
            for j, elem in enumerate(r):
                if elem == 1:
                    fresh.add((i, j))
                if elem == 2:
                    visit.add((i, j))
                    rotten.append((i, j, 0))
        
        if not fresh and not rotten:
            return 0

        q = deque(rotten)
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            i, j, length = q.popleft()
            if (i, j) in fresh:
                fresh.remove((i, j))
            if not fresh:
                return length
            mask1 = min(i, j) < 0
            mask2 = i >= m or j >= n
            # if OOB or current cell is empty
            if mask1 or mask2 or grid[i][j] == 0:
                continue
            for di, dj in dirs:
                if (i + di, j + dj) not in visit:
                    q.append((i + di, j + dj, length + 1))
                    visit.add((i + di, j + dj))
    
        return -1