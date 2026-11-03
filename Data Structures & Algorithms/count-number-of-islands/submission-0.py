class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        total_rows, total_columns = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                r,c = queue.popleft()
                for dr, dc in directions:
                    if (r + dr) in range(total_rows) and (c + dc) in range(total_columns) and (r + dr,c + dc) not in visited and grid[r + dr][c + dc] == "1":
                        queue.append((r + dr, c + dc))
                        visited.add((r+dr, c+dc))


        for r in range(total_rows):
            for c in range(total_columns):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands