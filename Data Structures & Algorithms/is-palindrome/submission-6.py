class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []
        for c in s:
            if c.isalpha() or c.isalnum():
                if c.isalpha():
                    c = c.lower()
                s1.append(c)
        start = 0
        end = len(s1) - 1
        mid = (start + end)// 2
        i = 0
        while i <= mid:
            if s1[start] != s1[end]:
                return False
            
            start += 1
            end -= 1
            i+= 1
        return True
        