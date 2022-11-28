import sys

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair cars with speeds
        paired = [(position[i], speed[i]) for i in range(len(position))]
        paired.sort(key = lambda x : x[0], reverse=True)

        time_to_dest = sys.maxsize
        fleets = 0
        temp = target

        for i in range(len(paired)):
            temp = (target - paired[i][0]) / paired[i][1]
            # print(temp)
            if i == 0:
                fleets += 1
                time_to_dest = temp
                continue
            if temp <= time_to_dest:
                continue
            fleets += 1
            time_to_dest = temp
            # print("b")
            
        return fleets
