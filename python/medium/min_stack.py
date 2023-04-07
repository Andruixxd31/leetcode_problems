class MinStack:

    def __init__(self):
        self.minStack = []
        self.minNum = 0
        

    def push(self, val: int) -> None:
        if len(self.minStack) == 0:
            self.minNum = val
        elif self.minNum > val:
            self.minNum = val
        self.minStack.append(val)

    def pop(self) -> None:
        if self.minStack.pop() == self.minNum:
            if len(self.minStack) > 0:
                self.minNum = self.minStack[0]
                for num in self.minStack:
                    if num < self.minNum:
                        self.minNum = num

    def top(self) -> int:
        return self.minStack[len(self.minStack)-1]

    def getMin(self) -> int:
        return self.minNum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
