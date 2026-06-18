class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        m1 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        m2 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        for i in range(len(s1)):   
            m1[s1[i]] += 1
            m2[s2[i]] += 1        

        matches = 0
        for i in range(26):
            ch = chr(ord('a') + i)
            matches += (1 if m1[ch] == m2[ch] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            
            
            ch_add = s2[r]
            ch_remove = s2[r - len(s1)]
            
            if m1[ch_add] == m2[ch_add]:
                matches -= 1
            m2[ch_add] += 1
            if m1[ch_add] == m2[ch_add]:
                matches += 1

            if m1[ch_remove] == m2[ch_remove]:
                matches -= 1
            m2[ch_remove] -= 1
            if m1[ch_remove] == m2[ch_remove]:
                matches += 1

        return matches == 26


