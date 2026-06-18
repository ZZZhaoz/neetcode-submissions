class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1 = {}
        mp2 = {}
        for s in s1:
            if s not in mp1:
                mp1[s] = 0
            mp1[s] += 1
        l = 0
        for r in range(len(s2)):
            if s2[r] not in mp2:
                mp2[s2[r]] = 0
            mp2[s2[r]] += 1
            
            if r - l + 1 > len(s1):
                mp2[s2[l]] -= 1
                if mp2[s2[l]] == 0:
                    del mp2[s2[l]]
                l += 1
            if mp1 == mp2:
                return True

        return False

        