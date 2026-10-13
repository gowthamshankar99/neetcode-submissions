class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        satisfied = 0
        window = 0 
        l = 0 
        max_cust = 0
        for r in range(len(grumpy)):
            if grumpy[r]:
                window += customers[r]
            else:
                satisfied += customers[r]

            if r - l + 1 > minutes:
                if grumpy[l]:
                    window = window - customers[l]
                l+=1
                

            max_cust = max(max_cust, window)

        return max_cust + satisfied




        