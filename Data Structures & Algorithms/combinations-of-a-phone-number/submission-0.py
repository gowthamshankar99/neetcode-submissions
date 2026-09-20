class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        map_m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        total, curr = [], []
        self.helper(map_m, total, digits, curr,0)
        return total

    def helper(self, map_m, total, digits, curr, index):
        if index == len(digits):
            total.append("".join(curr))
            return 

            # compare to the map 
        characters = map_m[digits[index]]
        for character in characters:
            # if character not in curr:
            curr.append(character)
            self.helper(map_m, total, digits, curr, index+1)
            curr.pop()
