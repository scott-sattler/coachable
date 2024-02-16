class BrowserHistory:
    def __init__(self, homepage: str):
        # homepage "leetcode.com"
        self.last = 0
        self.curr = 0
        self.history = [''] * 101
        self.history[0] = homepage

    def visit(self, url: str) -> None:
        # clears forward history
        self.curr += 1
        # if not self.curr < len(self.history):
        #     self.history.append(url)
        # else:
        #     self.history[self.curr] = url
        self.history[self.curr] = url
        self.last = self.curr
        return self.history[self.curr]

    def back(self, steps: int) -> str:
        # clamps to first page (homepage)
        self.curr -= steps
        if self.curr < 0:
            self.curr = 0
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        # clamps to last valid forward page
        self.curr += steps
        if self.curr > self.last:
            self.curr = self.last
        return self.history[self.curr]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
