class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        start = 0 
        end = num

        while start <= end:
            mid = (start + end)//2
            print(mid*mid)
            if mid*mid == num:
                return True
            elif mid*mid<num:
                
                start = mid+1
            else:
                end = mid-1
                

        return False
