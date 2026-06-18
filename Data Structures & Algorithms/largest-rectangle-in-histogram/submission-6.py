class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = []
        n= len(heights)
        # heights.append(1)
        for i in range(len(heights)):
            if not stack:
                stack.append((heights[i], i))
                res.append(heights[i])
            # else:
            #     a = stack[-1]
            #     if a[0] > heights[i]:
            #         a = stack.pop()
            #         start = a[1]
            #         j = 1
            #         while a[0] > heights[i]:
            #             res.append(a[0]*j)
            #             if stack:
            #                 a = stack.pop()
            #                 res.append(a[0])
            #                 j+=1
            #             else:
            #                 break
                        
            #             if  a[0] < heights[i]:
            #                 stack.append(a)
            #             else:
            #                 stack.append((heights[i], a[1]))
            #         stack.append((heights[i], i))
            #         res.append(heights[i])
            #         if stack:
            #             res.append(stack[-1][0]*(start - a[1] + 1))
            #     else:
            #         stack.append((heights[i], i))
                    
            #         res.append(heights[i])
            else:
                a = stack[-1]
                if a[0] > heights[i]:
                    start = a[1]
                    while stack and stack[-1][0] > heights[i]:
                        a = stack.pop()
                        width = i - a[1]
                        res.append(a[0] * width)
                        start = a[1]
                    stack.append((heights[i], start))
                    res.append(heights[i])
                else:
                    stack.append((heights[i], i))
                    res.append(heights[i])

        # if stack:
        #     start = stack[-1][1]
        # for i in range(len(stack) - 1, -1, -1):
        #     res.append(stack[i][0]*(start - stack[i][1] + 1))
        start = len(heights)
        while stack:
            a = stack.pop()
            width = start - a[1]
            res.append(a[0] * width)
        
        
        return max(res)
        