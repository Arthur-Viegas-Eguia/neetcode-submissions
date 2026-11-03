class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs(r,c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            area = 1
            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    if (r + dr) in range(rows) and (c + dc) in range(cols) and (r + dr, c + dc) not in visited and grid[dr + r][dc + c] == 1:
                        q.append((r + dr, c + dc))
                        visited.add((r+dr, c+dc))
                        area += 1
            return area
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    area = bfs(r, c)
                    maxArea = max(maxArea, area)
        return maxArea
        