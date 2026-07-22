class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        M, N = len(profit), capacity+1

        cache = [[-1]*N for _ in range(M)]
        max_profit = self.helper(0, profit, weight, capacity, cache)
        return max_profit

    def helper(self, index, profit, weight, capacity, cache):
        if index == len(profit):
            return 0

        # retrieve
        if cache[index][capacity] != -1:
            return cache[index][capacity]

        # skip
        max_profit = self.helper(index+1, profit, weight, capacity, cache)
        cache[index][capacity] = max_profit

        # dont skip 
        new_capacity  = capacity - weight[index]
        if new_capacity >=0:
            res = profit[index] + self.helper(index+1, profit, weight, new_capacity, cache)
            max_profit = max(max_profit, res)

            # update cache here
            cache[index][capacity] = max_profit

        return max_profit








