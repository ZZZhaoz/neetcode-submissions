class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        no = []
        res = 0
        while r < len(s):
            while s[r] in no:
                no.pop(0)
                l += 1
                    
            no.append(s[r])
            res = max(res, len(no))
            r += 1

        return res

        
        