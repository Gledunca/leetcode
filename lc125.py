import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = 0
        s = re.sub(r'[\W_]', '', s)
        s = s.lower()
        if len(s) % 2 == 0:
            i = (len(s) // 2) - 1
            j = (len(s) // 2)
        else:
            i = j = len(s) // 2
        while i >= 0:
            if s[i] != s[j]:
                return False
            i -= 1
            j += 1
        return True