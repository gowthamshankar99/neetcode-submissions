class Solution:

    
    def climbStairs(self, n: int) -> int:
        map = {}
        return self.helper(n, map)
    
    def helper(self, n, map):
        if n in map:
            return map[n]        

        if n == 1:
            return 1
        if n == 2:
            return 2

        map[n] = self.helper(n-1,map) + self.helper(n-2, map)

        return map[n]
         