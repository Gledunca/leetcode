class Solution:
    def ksum(self, nums: List[int], target: int, depth: int):
            results = []
            if depth == 2:
                # print("Target", target)
                # print("Nums", nums)
                d = {}
                for i in range(len(nums)):
                    if nums[i] in d:
                        k = d.get(nums[i])
                        res = [nums[k], nums[i]]
                        # print("Found", res)
                        results.append(res)
                    else:
                        # print("Adding to dict", target-nums[i], i)
                        d[target-nums[i]] = i
                return results
            cur = []
            for i in range(len(nums)):
                cur.append(nums[i])
                subsets = self.ksum(nums[i+1:], target-nums[i], depth-1)
                # print("Subsets", subsets)
                for s in subsets: 
                    a = cur+s
                    # print("Adding", a)
                    results.append(a)
                cur.pop(-1)
            return results
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        quads = self.ksum(nums, target, 4)
        sets = []
        uniq_quads = []
        for q in quads:
            if set(q) in sets:
                continue
            sets.append(set(q))
            uniq_quads.append(q)
        return uniq_quads
