class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for char in s:
            if char.isalpha() or char.isnumeric():
                s1+=char
       
        for i in range(int(len(s1)//2)):
            if s1[i].upper() != s1[len(s1) - i - 1].upper():
                return False
        return True