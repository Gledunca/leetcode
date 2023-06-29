class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for i in range(len(s)-1):
            # print(i)
            l = r = i
            while l < 0 and s[l-1] == s[i]:
                l -= 1
            while r<len(s)-1 and s[r+1] == s[i]:
                r += 1
            while l>0 and r<len(s)-1 and s[l-1] == s[r+1]:
                l-=1
                r+=1
            # print(l, r)
            res = s[l:r+1] if (r+1)-l > len(res) else res
        return res