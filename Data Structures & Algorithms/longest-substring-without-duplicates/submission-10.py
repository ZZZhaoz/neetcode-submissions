class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l, r = 0, 0
        m = []
        res = []
        while r < len(s):
            while s[r] in m:
                m.remove(s[l])
                l += 1    
            m.append(s[r])
            r += 1
            res.append(r-l)
        return max(res)