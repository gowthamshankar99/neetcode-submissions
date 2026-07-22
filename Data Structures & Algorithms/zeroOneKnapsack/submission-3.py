from functools import lru_cache
class Solution:
    

    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        self.profit = profit
        self.weight = weight        
        max_profit = self.helper(0, capacity)
        return max_profit 

    @lru_cache(None)
    def helper(self, index, capacity):
        if index == len(self.profit):
            return 0

        # skip
        max_profit = self.helper(index+1,capacity)

        new_capacity = capacity - self.weight[index]

        if new_capacity >= 0:
            current_profit = profit[index] + self.helper(index+1, new_capacity)
            max_profit = max(max_profit, current_profit)

        return max_profit




