class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0

        left = 0
        right = 1

        result = 0 


        for i in range(len(prices)-1):
            if prices[right] < prices[left]:
                left = right
                right = left+1
            else:
                result = max(result, prices[right]-prices[left])
                right = right+1
            


        return result



        