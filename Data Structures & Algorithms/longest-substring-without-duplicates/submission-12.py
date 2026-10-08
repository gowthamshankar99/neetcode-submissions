class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        exists = set()

        result = 0
        temp = 0

        for s_single in s:

            while s_single in exists:
                exists.remove(s[temp])
                temp += 1
            
            exists.add(s_single)
            result = max(result, len(exists))

        
        return result




            
        