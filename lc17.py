class Solution:
    def __init__(self):
        self.d = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "kjl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        self.res = []

    def helper(self, digits, cur, i):
        if i == len(digits):
            self.res.append(cur)
            return
        chs = self.d[digits[i]]
        for j in range(len(chs)):
            cur += chs[j]
            self.helper(digits, cur, i+1)
            cur = cur[:-1]
        return

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.helper(digits, "", 0)
        return self.res
