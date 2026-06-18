class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0

        res = 0
        m = {}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = 0
            m[s[i]] += 1
            while (i - l + 1) - max(m.values()) > k:
                m[s[l]] -= 1
                l += 1
            res = max(i - l + 1, res)

        return res