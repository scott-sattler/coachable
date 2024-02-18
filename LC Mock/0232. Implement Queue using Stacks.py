###################### static array with pointers ###################### # noqa
# time: O(1)
# space:
#   stream input O(n)
#   O(n) array space, where n is the maximum number of push inputs
#   for O(n) auxiliary space

class MyQueue:
    def __init__(self):
        self.queue = [0] * 100
        self.head = 0
        self.tail = 0

    def push(self, x: int) -> None:
        self.queue[self.tail] = x
        self.tail += 1

    def pop(self) -> int:
        self.head += 1
        return self.queue[self.head - 1]

    def peek(self) -> int:
        return self.queue[self.head]

    def empty(self) -> bool:
        return self.head == self.tail


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


################ naive: two stacks (problem expectation) ############### # noqa
# time:
#   O(n)
#   O(1) amortized
# space:
#   stream input
#   O(n) stack space
#   for O(n) auxiliary

class MyQueue:
    def __init__(self):
        self.primary = list()
        self.secondary = list()

    def push(self, x: int) -> None:
        while self.secondary:
            self.primary.append(self.secondary.pop())
        self.primary.append(x)

    def pop(self) -> int:
        while self.primary:
            self.secondary.append(self.primary.pop())
        return self.secondary.pop()

    def peek(self) -> int:
        if self.primary:
            return self.primary[0]
        return self.secondary[-1]

    def empty(self) -> bool:
        return not self.primary and not self.secondary

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
