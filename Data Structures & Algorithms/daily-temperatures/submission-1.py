class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i] , i))
            else:
                a = stack.pop()
                if temperatures[i] <= a[0]:
                    stack.append(a)
                    stack.append((temperatures[i], i))
                else:
                    while a[0] < temperatures[i]:

                        
                        res[a[1]] = i - a[1]
                        if stack:
                            a = stack.pop()
                        else:
                            break
                    if a[0] >= temperatures[i]:
                        stack.append(a)
                    stack.append((temperatures[i], i))
        return res

        