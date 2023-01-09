import bisect

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        # print(stones)
        while len(stones) > 1:
            print(stones)
            x = stones.pop(-1)
            y = stones.pop(-1)
            if x != y:
                bisect.insort_right(stones, abs(x-y))
        return stones[0] if stones else 0