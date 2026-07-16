class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)+1
        cols = len(text2)+1

        res = [[0]*cols for _ in range(rows)]

        for r in range(1, rows):
            for c in range(1, cols):
                if text1[r-1] == text2[c-1]:
                    res[r][c] = res[r-1][c-1]+1
                else:
                    res[r][c] = max(res[r-1][c], res[r][c-1])

        
        return res[rows-1][cols-1]

        


        