class Solution:

    
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        if n == 2:
            return 2
        
        val = n+1
        res = [0]*val
        # do the baseline
        res[1] = 1
        res[2] = 2

        for i in range(3,n+1):

            res[i] = res[i-1] + res[i-2]
        
        return res[n]
