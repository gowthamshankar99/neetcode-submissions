class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """

        start, end - initialize 

        x - 1
        y - 2


        length of the window - top occurance value in the map <= k 

        else 

        shrink the left side of the array
        delete the values from the map

        calc max value and return max value
        """

        res = 0
        left = 0
        right = 0
        map = {}


        while right < len(s):
            map[s[right]] = map.get(s[right], 0) + 1

            # get the max_value 
            max_occurance_value = self.calcMaxValue(map)
            if (right-left+1) - max_occurance_value <= k:
                res = max(res, (right-left+1))
                right +=1 
            else:
                # delete from map 
                map[s[left]] -= 1
                if map[s[left]] == 0:
                    del map[s[left]]
                left += 1
                right +=1                 


        return res



        

    def calcMaxValue(self, map):
        max_value = 0
        for key,value in map.items():
            max_value = max(max_value, value)
        
        return max_value
