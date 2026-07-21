class Solution:
    def longestPalindrome(self, s: str) -> int:

        map = {}

        for single in s:
            if single in map:
                map[single] += 1
            else:
                map[single] = 1
        
        print(map)

        # loop through the map 
        res = 0 
        is_one = False
        
        # loop through the map first and when you find a odd number 
        #- add the 1 to it 
        # and flip the flag 

        for key,value in map.items():

            # % 2 == 0 

            # % 2 != 0 and > 1

            # == 1
            if value % 2 == 0:
                res = res + value 
            elif value > 1:
                res += value - 1
                is_one = True
            else:
                is_one = True

        
        return res if not is_one else res+1
        