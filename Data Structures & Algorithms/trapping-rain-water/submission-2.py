class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0]*len(height)
        suffix = [0]*len(height)
        prefix[0] = height[0]
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i])
        suffix[n - 1] = height[n - 1]
        for j in range(len(height) - 2, -1, -1):
            suffix[j] = max(suffix[j + 1], height[j])
        # prefix.insert(0, 0)
        
        total = 0
        
        # suffix.insert(0, 0)
        for z in range(len(height)):

            total += min(prefix[z], suffix[z]) - height[z]
        return total
        
