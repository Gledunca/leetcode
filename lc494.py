class Solution:
    def helper(self, nums, ind, cur, target, d) -> int:
        if ind == len(nums):
            return 1 if cur == target else 0
        if (ind, cur) in d:
            return d[(ind, cur)]
        d[(ind, cur)] = self.helper(nums, ind+1, cur+nums[ind], target, d) + self.helper(nums, ind+1, cur-nums[ind], target, d)
        return d[(ind, cur)]
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = self.helper(nums, 0, 0, target, {})
        #print(self.d)
        return res