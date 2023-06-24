import copy

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        d = {0: 0}
        for r in rods:
            nd = copy.deepcopy(d)
            for (diff, tall) in d.items():
                short = tall-diff
                nd[diff+r] = max(nd.get(diff+r, 0), tall+r)
                newdiff = abs(short+r-tall)
                newtall = max(tall, short+r)
                nd[newdiff] = max(nd.get(newdiff, 0), newtall)
            d = nd

        return d[0]