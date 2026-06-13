class Solution:
    def validPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s)-1


        while start < end:
            if s[start] == s[end]:
                start = start + 1
                end = end - 1
            else:
                if self.valid(s[start+1:end+1]) or self.valid(s[start:end]):
                    return True
                else:
                    return False

        return True

    def valid(self, s):

        result = list(s)
        start = 0
        end = len(s)-1

        while start < end:
            result[start] = s[end]
            result[end] = s[start]

            start = start + 1
            end = end - 1

        if ''.join(result) == s:
            return True
        else:
            return False
        
