class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.mini = None
        

    def push(self, val: int) -> None:
        self.stack1.append(val)
        # if self.mini is None or val < self.mini:
        #     self.mini = val
        if self.stack2 != []:
            a = self.stack2.pop()
            if a < val:
                self.stack2.append(a)
                self.stack2.append(a)
            else:
                self.stack2.append(a)
                self.stack2.append(val)

        else:
            self.stack2.append(val)

     
            

        

    def pop(self) -> None:
        self.stack1.pop()
        self.stack2.pop()
        

    def top(self) -> int:
        a = self.stack1.pop()
        self.stack1.append(a)
        self.stack1.append(a)
        
        return self.stack1.pop()

        

    def getMin(self) -> int:
        a = self.stack2.pop()
        self.stack2.append(a)
        return a
        
