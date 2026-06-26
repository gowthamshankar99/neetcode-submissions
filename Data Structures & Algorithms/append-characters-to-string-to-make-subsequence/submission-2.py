class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
            compare s and t 

            move each character until you cant find a character of t in s - 

            just move character of s until that cahracter is found if not found until thne end - append it 
        """

        s_counter = 0
        t_counter = 0 

        while s_counter < len(s) and t_counter < len(t):
            if s[s_counter] == t[t_counter]:
                s_counter += 1
                t_counter += 1
            else:
                # if they are not equal - just increment s
                s_counter += 1


        return len(t)-t_counter


