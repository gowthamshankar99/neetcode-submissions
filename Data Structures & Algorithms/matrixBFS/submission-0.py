class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        queue = deque()
        

        queue.append((0,0))
        visited.add((0,0))

        length = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft();
                if r == ROW - 1 and c == COL - 1:
                    return length
                neighbors = [[0,1],[1,0], [-1,0], [0,-1]]

                for dr, dc in neighbors:
                    if (min(r+dr, c+dc) < 0 or r+dr == ROW or c+dc == COL or (r+dr, c+dc) in visited or grid[r+dr][c+dc] == 1):
                        continue
                    
                    queue.append((r+dr, c+dc))
                    visited.add((r+dr,c+dc))



            length = length + 1

        return -1


        
        