class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in d:
                        if (dr + r) in range(rows) and (dc + c) in range(cols) and (r + dr, c + dc) not in visited and grid[r + dr][c + dc] == "1":
                            q.append((r + dr, c + dc))
                            visited.add((r + dr, c + dc))
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
        return count