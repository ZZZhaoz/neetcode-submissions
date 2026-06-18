class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = 0
        l, r = 0, 0
        window = {}
        max_key = 0
        while r < len(s):
            window[s[r]] = 1 + window.get(s[r], 0)
            max_key = max(window[s[r]] , max_key)
            while r - l + 1 - max_key > k:
                window[s[l]] -= 1
                l += 1

                

            mp = max(mp, r - l + 1)
            r += 1
        return mp
    