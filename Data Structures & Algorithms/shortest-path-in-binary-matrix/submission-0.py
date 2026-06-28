from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        if grid[0][0] or grid[ROW-1][COL-1]:
            return -1

        length = 1
        queue = deque()
        queue.append((0,0, length))
        visited = set()
        visited.add((0,0))

        
        

        while queue:
            size = len(queue)
            for i in range(size):

                r,c, length = queue.popleft()
                if r == ROW-1 and c == COL-1:
                    return length

                directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]

                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if min(nr,nc) < 0 or nr == ROW or nc == COL or (nr,nc) in visited or grid[nr][nc] == 1:
                        continue
                    
                    print((nr,nc))
                    queue.append((nr,nc, length+1))
                    visited.add((nr,nc))

        return -1


                


        
        

        