class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = 0
        h = 0
        d = {0: -1}
        for i in range(len(s)):
            h = h+1 if s[i] == "(" else h-1
            if h < 0:
                h = 0
                d = {0: i}
                continue
            if h in d and s[i] == ")":
                l = max(l, i-d[h])
                continue
            d[h] = i
        return l
