class Solution:
    def confusingNumber(self, n: int) -> bool:
        map = {'1': '1', '2': '2', '6': '9', '8': '8', '9': '6', '0': '0'}
        res = ""
        for num in str(n):
            if num not in map:
                return False
            else:
                res += map[num]
                
        # valid number at this point
        if res == "".join(reversed(str(n))):
            return False
        
        return True
        