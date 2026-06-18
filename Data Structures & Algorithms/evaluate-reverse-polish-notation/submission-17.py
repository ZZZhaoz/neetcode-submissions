class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for num in tokens:
          
               
            if num == '+':
                a = stack.pop()

                b = stack.pop()

                stack.append(int(b)+int(a))
            elif num =='-':
                a = stack.pop()

                b = stack.pop()
                stack.append(int(b)-int(a))
            elif num == '*':
                a = stack.pop()

                b = stack.pop()
                stack.append(int(b)*int(a))
            elif num == '/':
                a = stack.pop()

                b = stack.pop()
                
                stack.append(int(int(b)/int(a)))
            else:
                stack.append(int(num))
        return stack[0]
                

                 

        