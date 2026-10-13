class Solution:
    def arrangeCoins(self, n: int) -> int:

        # k ( k + 1) / 2
        result = 1
        temp = 1
        
        while True:

            temp = result * (result + 1)/2

            if temp > n:
                return result-1
                
            else:
                result += 1

        


        

        