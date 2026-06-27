class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        stack = []

        def bc(op, cl):
            if op == cl == n:
                answer.append("".join(stack))
                return answer
            
            if op < n:
                stack.append("(")
                bc(op + 1, cl)
                stack.pop()

            if cl < op:
                stack.append(")")
                bc(op, cl + 1)
                stack.pop()
        
        bc(0, 0)
        return answer