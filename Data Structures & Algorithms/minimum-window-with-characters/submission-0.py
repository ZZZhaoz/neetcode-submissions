class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="":
            return ""
        
        mp1 = {}
        mp2 = {}
        for c in t:
            if c not in mp1:
                mp1[c] = 0
            mp1[c] += 1

        l = 0
        have, need = 0, len(mp1)
        res, reslen = [-1, -1], float("infinity")
        for r in range(len(s)):
            c= s[r]
            if c not in mp2:
                mp2[c] = 0
            mp2[c] += 1

            if c in mp1 and mp1[c] == mp2[c]:
                have+=1
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                mp2[s[l]] -= 1
                if s[l] in mp1 and mp2[s[l]] < mp1[s[l]]:
                    have -= 1
                l+= 1

        l, r = res
        return s[l:r+1] if reslen != float("infinity") else ""
        