class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        for single in s:
            if single in map:
                map[single] = map[single] + 1
            else:
                map[single] = 1

        for single in t:
            if single in map:
                map[single] = map[single] - 1
            else:
                return False     


        for key,value in map.items():
            if value != 0:
                return False

        return True     


        