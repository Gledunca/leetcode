class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = {}
        for item in nums:
            d[item] = item
        for i in range(len(nums) + 1):
            if i not in d:
                return i
            else:
                continue
        return None
        