import copy
class Solution:


    def combine(self, n: int, k: int) -> List[List[int]]:
        # List of the nums youll be iterating over
        l = [i+1 for i in range(n)]
        res = []

        def helper(l, cur) -> None:
            # print(l, cur, res)
            if not l:
                return
            if len(cur)+1 == k:
                for n in l:
                    res.append(cur + [n])
                return
            ln = len(l)
            while l:
                cur.append(l.pop(0))
                helper(copy.deepcopy(l), cur)
                cur.pop(-1)
            return

        helper(l, [])
        return res