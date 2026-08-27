class MinStack:
    stack = []
    prefix = []


    def __init__(self):
        self.stack = list()
        self.prefix = list()
        

    def push(self, val: int) -> None:
        #The element to be pushed onto the top of the stack 

        if (len(self.prefix) > 0):
            self.prefix.append(min(self.prefix[-1], val))
        else: 
            self.prefix.append(val)
        self.stack.append(val)

        return None
        

    def pop(self) -> None:
        self.stack.pop()
        self.prefix.pop()
        return None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefix[-1]
        
