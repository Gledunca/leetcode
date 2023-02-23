class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        i, j = nums[0], nums[1]
        for n in nums[2:]:
            temp = max(n+i, j)
            print(i, j, temp)
            i = max(i, j)
            j = temp
        return j