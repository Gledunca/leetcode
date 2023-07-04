class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        full_sum = sum(nums)
        nums = list(set(nums))
        unique_sum = 3*sum(nums)
        return (unique_sum-full_sum) // 2
