class Solution:
    def isValid(self, s: str) -> bool:

        stack1 = []
        
        for char in s:
            if char in ['[', '{', '(']:
                stack1.append(char)
            elif char in [']', '}', ')']:
                if stack1 == []:
                    return False
                a = stack1.pop()
               
                if a + char not in ['[]', '{}', '()']:
                    return False
            
        if stack1 != []:
            return False
        return True
                    
