class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        currCombination, totalCombination = [], []
        self.helper(1, currCombination, totalCombination, n, k)
        return totalCombination



    def helper(self, i, currCombination, totalCombination, n ,k):
        if len(currCombination) == k:
            totalCombination.append(currCombination.copy())
            return
        
        if i > n:
            return 

        currCombination.append(i)            

        self.helper(i+1, currCombination, totalCombination,n,k)

        currCombination.pop()

        self.helper(i+1, currCombination, totalCombination,n,k)



        