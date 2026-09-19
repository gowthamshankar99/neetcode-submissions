class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr, total = [],[]
        self.helper(curr, total, n)
        return total

    def helper(self, curr, total, n):
        if curr.count("(") == n and curr.count(")") == n:
            total.append(''.join(curr.copy()))
            return

        if curr.count("(") != n:
            curr.append("(")
            self.helper(curr, total, n)
            curr.pop()

        if curr.count(")") != n and curr.count(")") < curr.count("("):
            curr.append(")")
            self.helper(curr, total, n)
            curr.pop()

        
            