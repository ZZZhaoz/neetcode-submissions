class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l, r = 0, 0
        res = 0
        while r < len(s):
            if s[r] not in mp:
                mp[s[r]] = 1
            else:
                while l < r and s[r] in mp: 
                    del mp[s[l]]
                    l += 1
                mp[s[r]] = 1
            res = max(r - l + 1, res)
            r += 1
            
        return res