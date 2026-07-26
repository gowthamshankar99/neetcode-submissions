from functools import cmp_to_key 

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = []
        def sorting_function(n1,n2):

            if n1+n2 > n2+n1:
                return -1
            else:
                return 1        
        for i,n in enumerate(nums):
            res.append(str(n))
        
        res = sorted(res, key=cmp_to_key(sorting_function))
        return str(int("".join(res)))


    def sorting_function(self, n1,n2):

        if n1+n2 > n2+n1:
            return -1
        else:
            return 1




        