class MinStack:

    def __init__(self):
        self.l = []
        self.stack = []
       
        
    def push(self, val: int) -> None:
        self.l.append(val)
        if self.stack:
            a = self.stack[-1]
            val = min(a, val)
        self.stack.append(val)

    def pop(self) -> None:
        self.l.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.l[-1]
        
    def getMin(self) -> int:
        return self.stack[-1]
       
      
        
