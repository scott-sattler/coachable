'''
size k
 0  1  2  3  4  5  6  7
[-1, -1, -1, -1, -1, -1]

init with -1 array of size k


 0  1  2  3  4  5  6  7
[-1, -1, -1, -1, -1, -1]
  ^
head
tail


 0  1  2  3  4  5  6  7
[5, -1, -1, -1, -1, -1]
 ^   ^
head
    tail


[5, -1, -1, -1, -1, -1]
     ^               ^
                    head
    tail

 0  1  2  3  4  5  6  7
[5, 6, -1, -1, -1, -1]
 ^      ^
head
       tail


 0  1  2  3  4  5  6  7
[5, 6, -1, -1, -1, 2]
        ^          ^
                  head
       tail



 0  1  2  3  4  5  6  7
[5, 6, 7, 5, 2, 4]
 ^
head
tail





[5, 6, -1, 5, 2, 4]
        ^
       head
       tail


[5, 6, 7, 5, 2, 4]
    ^  ^
   head
      tail



[5, 6, -1, 5, 2, 4]
    ^      ^
   head
          tail

tail inserts right
tail removes left

head inserts left
head removes right



[5, -1, -1, -1, -1, 9]
     ^              ^
                   head
    tail




[5, 8, 2, 4, 6, 9]
       ^  ^
      head
          tail


 12345
 ^   ^
[5, 1, 2, 3, 4]
 ^  ^
head
     tail


'''


class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.deq = [-1] * k
        self.head = 0
        self.tail = (self.head + 1) % k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deq[self.head] = value
        self.head = (self.head - 1) % self.k  # move left
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deq[self.tail] = value
        self.tail = (self.tail + 1) % self.k  # move right
        return True

    def deleteFront(self) -> bool:
        print(self.deq, self.head, self.tail)
        if self.isEmpty():
            print('foo')
            return False
        self.head = (self.head + 1) % self.k
        self.deq[self.head] = -1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1) % self.k
        self.deq[self.tail] = -1
        return True

    def getFront(self) -> int:
        return self.deq[(self.head + 1) % self.k]

    def getRear(self) -> int:
        return self.deq[(self.tail - 1) % self.k]

    def isEmpty(self) -> bool:
        right = (self.head + 1) % self.k
        left = (self.tail - 1) % self.k
        if self.deq[right] == self.deq[left] == -1:
            return True
        return False

    def isFull(self) -> bool:
        if self.deq[self.head] != -1 and self.deq[self.tail] != -1:
            return True
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
