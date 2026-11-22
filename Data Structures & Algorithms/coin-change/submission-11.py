class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        count = 0
        memo = {}
        res = self.helper(coins, amount, memo)
        
        return res if res != float('inf') else -1

    def helper(self, coins, amount, memo):
        if amount in memo:
            return memo[amount]

        if amount < 0:
            return float('inf')
        elif amount == 0:
            return 0

        min_val = float('inf')

        for coin in coins:
            res = self.helper(coins, amount-coin, memo)
            # store values in the cache
            min_val = min(res+1, min_val)
        
        memo[amount] = min_val

        return min_val


        