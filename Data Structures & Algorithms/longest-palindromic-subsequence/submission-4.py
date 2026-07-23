class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        len_string = len(s)

        res = [[0]*len_string for _ in range(len_string)]

        ROW = len(res)
        COL = len(res[0])

        for i in range(ROW):
            res[i][i] = 1
            
        for r in range(len_string - 1, -1, -1):
            for c in range(r + 1, len_string):
                if s[r] == s[c]:
                    res[r][c] = 2 + res[r+1][c-1]
                else:
                    res[r][c] = max(res[r][c-1], res[r+1][c])

    

        return res[0][len_string-1]


        #T O T A L
        