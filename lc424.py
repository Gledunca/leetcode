class Solution:
    def last(self, l: list):
        return l[-1]
    def characterReplacement(self, s: str, k: int) -> int:
        chars_in_view = {}
        r = 0
        l = 0
        d = {}
        maxchar = s[0]
        maxfreq = 1
        while r < len(s):
            d[s[r]] = d.get(s[r], 0) + 1
            if d[s[r]] > maxfreq:
                maxfreq = d[s[r]]
                maxchar = s[r]
            if (len(s[l:r])+1) - maxfreq > k:
                d[s[l]] -= 1
                if s[l] == maxchar:
                    maxfreq -= 1
                if d[s[r]] > maxfreq:
                    maxchar = s[r]
                    maxfreq = d[s[r]]
                l += 1
            r += 1
        return r-l
