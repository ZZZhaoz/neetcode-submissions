class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = []
        l, r = 0, len(heights) - 1
        curr = min(heights[r], heights[l]) * (r -l)
        res.append(curr)
        while  l<r :
            
            if heights[r] > heights[l]:
                l += 1
               
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                r -= 1
            res.append(min(heights[r], heights[l]) * (r -l))
        return max(res)
