class MinStack:

    def __init__(self):
        self._min = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self._min) == 0:
            self._min.append(val)
        elif self._min[-1] >= val:
            self._min.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self._min[-1]:
            self._min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()