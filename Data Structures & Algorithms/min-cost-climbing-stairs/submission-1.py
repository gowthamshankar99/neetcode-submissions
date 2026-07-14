class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        """

        [1,2,3]

        res[0] = 1
        res[1] = 2

        [1,2,1]

        min(res[i-1], res[i-2]+nums[i])
        """

        res = [0]*len(cost)
        res[0] = cost[0]
        res[1] = cost[1]
    
        for i in range(2,len(cost)):
            res[i] = cost[i] + min(res[i-1], res[i-2])


        return min(res[len(cost)-2], res[len(cost)-1])




        