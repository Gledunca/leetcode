class Solution:
    def __init__(self):
        self.d = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in self.d:
            return self.d[amount]
        minimum = sys.maxsize
        bottom = -sys.maxsize
        for coin in coins:
            bottom = 1+self.coinChange(coins, amount-coin)
            if bottom < minimum and bottom > 0:
                minimum = bottom
        if minimum > 0 and minimum < sys.maxsize:
            self.d[amount]=minimum
        else:
            minimum = -1
            self.d[amount]=minimum
        return minimum