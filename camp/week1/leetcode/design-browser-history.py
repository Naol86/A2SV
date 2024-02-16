class BrowserHistory:

    def __init__(self, homepage: str):
        self.pos = 0
        self.lis = [homepage]

    def visit(self, url: str) -> None:
        if self.pos < len(self.lis) - 1:
            self.lis = self.lis[:self.pos + 1]
        self.lis.append(url)
        self.pos += 1

    def back(self, steps: int) -> str:
        if self.pos < steps:
            self.pos = 0
            return self.lis[0]
        else:
            self.pos -= steps
            return self.lis[self.pos]

    def forward(self, steps: int) -> str:
        if len(self.lis) - self.pos - 1 < steps:
            self.pos = len(self.lis) - 1
            return self.lis[-1]
        else:
            self.pos += steps
            return self.lis[self.pos]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)