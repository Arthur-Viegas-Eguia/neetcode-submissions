class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        dist = 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for dr, dc in d:
                    if (r + dr) in range(rows) and (c + dc) in range(cols) and (r + dr, c + dc) not in visited and grid[r+dr][c+dc] != -1:
                        q.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
                        grid[r+dr][c+dc] = dist
            dist += 1