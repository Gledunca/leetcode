class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        a = 0
        d = set()
        for b in range(len(s)):
            if s[b] not in d:
                d.add(s[b])
            else:
                res = max(b-a, res)
                while s[b] in d:
                    d.remove(s[a])
                    a += 1
                d.add(s[b])
        res = max(res, len(s)-a)
        return res