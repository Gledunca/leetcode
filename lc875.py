import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l != r:
            k = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p/k)
                if time > h:
                    break
            if time > h:
                l = k+1
            else:
                r = k
        return l
