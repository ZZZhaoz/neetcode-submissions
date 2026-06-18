class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(position)):
            time.append((position[i], (target - position[i]) / speed[i]))
        fleet = 0
        i = 0
        time.sort(key=lambda x: x[0], reverse=True)
        while i <= len(time) - 1:
            cur = time[i][1]
            while i + 1 <= len(time) - 1 and time[i + 1][1] <= cur:
                i += 1

            fleet += 1
            i+= 1
        return fleet
