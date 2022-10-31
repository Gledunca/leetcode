class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        res = 0
        for i in prices[1:]:
            m = min(m, i)
            res = max(res, i-m)
        return res
