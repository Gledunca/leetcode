class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        up = [nums[0]]
        down = [nums[-1]]

        for i in range(1, len(nums)):
            up.append(up[-1] * nums[i])

        for i in range(len(nums)-2, -1, -1):
            down.insert(0, down[0] * nums[i])

        nums[0] = down[1]
        nums[-1] = up[-2]
        for i in range(1, len(nums)-1):
            nums[i] = up[i-1] * down[i+1]

        return nums