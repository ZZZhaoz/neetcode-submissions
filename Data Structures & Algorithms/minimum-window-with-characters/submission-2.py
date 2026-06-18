class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        count = {}
        window = {}

        for c in t:
            if c not in count:
                count[c] = 0
            count[c] += 1
        
        have, need = 0, len(count)
        l = 0
        res, reslen = [-1, -1], float("infinity")

        for r in range(len(s)):
            if s[r] not in window:
                window[s[r]] = 0
            window[s[r]] += 1

            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1

                if s[l] in count and window[s[l]] == count[s[l]]:
                    have -= 1
                window[s[l]] -= 1

                l += 1

        l, r = res
        if reslen != float("infinity"):
            return s[l:r+1]
        else:
            return ""



        