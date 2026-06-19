class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
        
            cur = temperatures[i]
            if stack:
                while stack and stack[-1][1] < cur:
                    a = stack.pop()
                    answer[a[0]] = i - a[0] 

            stack.append((i, temperatures[i]))
        return answer


