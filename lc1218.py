class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # Memory solution
        res = 0
        d = {arr[0]: 1}
        for i in arr:
            if d.get(i, 0):
                res = max(res, d[i])
                d[i+difference] = d[i]+1
            else:
                d[i+difference] = 2
        return res