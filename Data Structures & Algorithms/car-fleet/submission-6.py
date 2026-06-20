class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        cars = sorted(zip(position, speed), reverse=True)
        for p, s in cars:
            time.append((target - p)/s)
        stack = []
        for t in time:
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)
        
