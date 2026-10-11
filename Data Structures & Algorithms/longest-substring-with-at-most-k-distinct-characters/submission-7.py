class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        """
            use a hashmap 
            fill the hashmap while loop through 


        """

        if k == 0:
            return 0

        map = {}
        res  = 0
        temp = 0

        for i in range(len(s)):
            map[s[i]] = map.get(s[i], 0)+1 
            if len(map) > k:
                # while loop 
                
                while len(map) > k:
                    map[s[temp]] = map[s[temp]] - 1
                    if map[s[temp]] == 0:
                        del map[s[temp]]
                    temp += 1
                        
                

            else:
                res = max(res, i - temp + 1)
        


        return res

            






        



        