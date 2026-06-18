class Solution:
    def isValid(self, s: str) -> bool:

        stack1 = []
        s1 = []
        for char in s:
            s1.append(char)
        for char in s1:
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
                    
        
        # for char1 in s:
        #     a = stack.pop()
        #     if char1 + a not in ['[]', '{}', '()']:
        #         return False
        # return True

