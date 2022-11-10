class Solution:
    def trap(self, height: List[int]) -> int:

        # Uses high points on either side of the dataset to find water storage space

        # Represents the highest current left bound
        lMax = height[0]
        # Highest current right bound
        rMax = height[-1]
        # Current left
        l = 0
        # Current right
        r = len(height)-1
        # Result
        res = 0
        while l < r:
            if lMax <= rMax:
                # Advance the left pointer in search of a higher bound than the right side
                l += 1
                # If water can be stored, lMax will not change and there will be a difference.
                lMax = max(lMax, height[l])
                # In the case that no water can be stored with the change, lMax will have already been
                # set to height[l], making for 0 change.
                res += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]
        return res
