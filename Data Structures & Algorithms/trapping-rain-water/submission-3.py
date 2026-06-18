class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r= 0, len(height) - 1
        maxl = height[l]
        maxr = height[r]
        answer = 0
        while l < r:
        
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                answer += maxl - height[l]

            else:
                r -= 1
                maxr = max(maxr, height[r])
                answer += maxr - height[r]

        
        return answer


        