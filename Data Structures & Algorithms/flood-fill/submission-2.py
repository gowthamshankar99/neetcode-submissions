class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ROW, COL = len(image), len(image[0])
        visited = set()
        starting_color = image[sr][sc]

        return self.dfs(ROW, COL, image, sr, sc, color, visited, starting_color)


    def dfs(self, ROW, COL, image, sr, sc, color, visited, starting_color):

        if sr < 0 or sc < 0 or sr >= ROW or sc >= COL or (sr, sc) in visited or image[sr][sc] != starting_color:
            return 

        visited.add((sr,sc))
        # change the color
        image[sr][sc] = color

        self.dfs(ROW, COL, image, sr+1, sc, color, visited, starting_color)
        self.dfs(ROW, COL, image, sr-1, sc, color, visited, starting_color)
        self.dfs(ROW, COL, image, sr, sc+1, color, visited, starting_color)
        self.dfs(ROW, COL, image, sr, sc-1, color, visited, starting_color)


        return image







