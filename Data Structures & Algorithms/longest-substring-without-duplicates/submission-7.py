class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        no = set()
        res = 0
        while r < len(s):
            while s[r] in no:
                no.remove(s[l])
                l += 1
                    
            no.add(s[r])
            res = max(res, r - l + 1)
            r += 1

        return res

        
        