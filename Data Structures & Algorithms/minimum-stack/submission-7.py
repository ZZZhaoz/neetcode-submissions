class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mini is None or val < self.mini:
            self.mini = val

        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        a = self.stack.pop()
        self.stack.append(a)
        self.stack.append(a)
        
        return self.stack.pop()

        

    def getMin(self) -> int:
        
        return min(self.stack)
        
