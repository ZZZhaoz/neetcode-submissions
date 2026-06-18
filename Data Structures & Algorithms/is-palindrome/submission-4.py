class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not(s[l].isalpha() or s[l].isnumeric()) and l < r:
                l += 1
            while not(s[r].isalpha() or s[r].isnumeric()) and l < r: 
                r -= 1
            if s[r].upper() != s[l].upper():
                return False
            l+= 1
            r-=1
        return True
        # s1 = ""
        # for char in s:
        #     if char.isalpha() or char.isnumeric():
        #         s1+=char
       
        # for i in range(int(len(s1)//2)):
        #     if s1[i].upper() != s1[len(s1) - i - 1].upper():
        #         return False
        # return True