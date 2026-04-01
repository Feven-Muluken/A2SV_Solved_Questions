class BrowserHistory:
    import webbrowser

    def __init__(self, homepage: str):
        self.continer = [homepage]
        self.num = 0

    def visit(self, url: str) -> None:
        self.num += 1
        self.continer = self.continer[:self.num]
        self.continer.append(url)


    def back(self, steps: int) -> str:
        self.num = max(0, self.num - steps)
        if self.num >= len(self.continer):
            self.num = len(self.continer - 1)
        return self.continer[self.num]
    def forward(self, steps: int) -> str:
        self.num += steps
        if self.num >= len(self.continer):
            self.num = len(self.continer) - 1
            
            return self.continer[self.num]
        else:
            return self.continer[self.num]
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)