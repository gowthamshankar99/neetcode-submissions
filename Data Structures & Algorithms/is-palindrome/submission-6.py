class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = ""

        for single in s:
            if single.isalnum():
                new_s = new_s + single

        new_s = new_s.lower()

        start = 0
        end = len(new_s)-1

        while start < end:
            if new_s[start] == new_s[end]:
                start += 1
                end -= 1
            else:
                return False

        return True

        

        