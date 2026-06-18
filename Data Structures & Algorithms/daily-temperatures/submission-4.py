class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        i = 0
        for temp in temperatures:
            stack.append((temp, i))
            i += 1
        
        answer = [0 for _ in range(len(temperatures))]
        
        s = []
        i = 0
        # while i <= len(temperatures) - 1:
        #     t = stack[i]
        #     if s == []:
        #         s.append(t)
        #     else:
        #         a = s.pop()
        #         resolved = False
        #         if a[0] < t[0]:      
                
        #             while a[0] < t[0]:
        #                 days = t[1] - a[1]
        #                 answer[a[1]] = days
        #                 if s:
        #                     a = s.pop()
        #                 else:
        #                     resolved = True
        #                     break
        #         if not resolved:
        #             s.append(a)
        #         s.append(t)

        #     i += 1

        while i <= len(temperatures) - 1:
            t = stack[i]
            while s and t[0] > s[-1][0]:
                a = s.pop()
                answer[a[1]] = t[1] - a[1]  

            s.append(t)
            i += 1
        return answer

