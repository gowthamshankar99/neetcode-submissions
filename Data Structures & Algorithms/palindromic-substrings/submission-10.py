class Solution:
    def countSubstrings(self, s: str) -> int:

        len_s = len(s)
        count = 0
        for i in range(len_s):
            for j in range(i, len(s)):
                if self.is_palindrome(i, j, s):
                    count += 1

        return count


    def is_palindrome(self, start, end, s):
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1

            else:
                return False

        return True

        