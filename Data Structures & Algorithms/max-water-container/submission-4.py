class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = (r - l) * min(heights[l], heights[r])
        while l < r:
            res1 = (r - l) * min(heights[l], heights[r])
            res = max(res, res1)
            if heights[l] < heights[r]:
                l += 1   
            else:
                r -= 1   
        return res



        
        