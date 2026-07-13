class Solution:

    
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        res =  [0] * (n+1)

        res[1] = 1
        res[2] = 2

        for i in range(3,n+1):
            res[i] = res[i-1] + res[i-2]

        return res[n]


        # map = {}
        # return self.helper(n, map)
    
    def helper(self, n, map):
        if n in map:
            return map[n]        

        if n == 1:
            return 1
        if n == 2:
            return 2

        map[n] = self.helper(n-1,map) + self.helper(n-2, map)

        return map[n]
         