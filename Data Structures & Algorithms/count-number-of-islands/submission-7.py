class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0;

        visited = set()
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    self.bfs(grid, r, c, visited)
                    count = count + 1

        return count

    def bfs(self, grid, r, c, visited):
        queue = deque([(r,c)])
        visited.add((r,c))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] == "1":
                    visited.add((nr,nc))
                    queue.append((nr, nc))

        return 1
