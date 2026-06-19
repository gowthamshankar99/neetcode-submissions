class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned_text = "".join(char for char in s if char.isalnum())
        cleaned_text = cleaned_text.lower()

        start = 0
        end = len(cleaned_text)-1
        while start < end:
            if cleaned_text[start] == cleaned_text[end]:
                start = start + 1
                end = end - 1
            else:
                return False

        return True

        