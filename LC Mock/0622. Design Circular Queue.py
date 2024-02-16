############################ array solution ############################ # noqa

class MyCircularQueue:
    def __init__(self, k: int):
        self.size = 0
        self.head = 0
        self.tail = 0
        self.cque = [-1] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.cque[self.tail] = value
        self.tail = (self.tail + 1) % len(self.cque)
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.cque[self.head] = -1
        self.head = (self.head + 1) % len(self.cque)
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.cque[self.head]

    def Rear(self) -> int:
        return self.cque[(self.tail - 1) % len(self.cque)]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.cque)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


############################# node solution ############################ # noqa

class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt


class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = Node(None)
        self.tail_pointer = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.tail_pointer.next = Node(value)  # create new node
        self.tail_pointer = self.tail_pointer.next  # update tail address
        self.tail_pointer.next = self.head.next  # point last to first
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size < 1:
            return False

        if self.size == 1:
            self.tail_pointer = self.head
            self.head.next = None
        else:  # self.size > 1
            self.head.next = self.head.next.next
            self.tail_pointer.next = self.head.next

        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail_pointer.val

    def isEmpty(self) -> bool:
        if self.size < 1:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.capacity:
            return True
        return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
