class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = 0
        l, r = 0, 0
        window = {}
        while r < len(s):
            if s[r] in window:
                while s[r] in window:
                    if s[l] in window:
                        del window[s[l]]
                    l += 1
           
            window[s[r]] = 1
            mp = max(mp, r - l + 1)
            r += 1
        return mp