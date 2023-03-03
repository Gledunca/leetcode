class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        t = []
        for key in d.keys():
            t.append([key, d[key]])
        t.sort(key=lambda x: x[1], reverse=True)
        res = [t[k][0] for k in range(k)]
        return res