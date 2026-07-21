class Solution:
    def countSubstrings(self, s: str) -> int:
        map = {}
        count = 0
        n = len(s)
        for i in range(n):
            for j in range(i,n):
                if self.is_palindrome(s,i,j, map):
                    count += 1
        
        return count
        

    def is_palindrome(self,s, i, j, map):

        if (i,j) in map:
            return map[(i,j)]

        
        if i >= j:
            map[(i,j)] = True
            return True

        if s[i] != s[j]:
            map[(i,j)] = False
            return False
        result = self.is_palindrome(s, i+1, j-1, map)
        map[(i, j)] = result

        return result
        