import random as r


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


class RandomizedSet:

    def __init__(self):
        self.index = dict()
        self.element = list()

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False

        # store index location
        val_index = len(self.element)
        # append to list
        self.element.append(val)
        # create dictionary entry
        self.index[val] = val_index
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False

        # get the element index
        val_index = self.index[val]
        # do swap operation to maintain O(1) time
        self.element[val_index], self.element[-1] = self.element[-1], self.element[val_index]
        # update swap element dictionary entry
        self.index[self.element[val_index]] = val_index
        # remove dictionary entry
        del self.index[val]
        # remove element from list
        self.element.pop()
        return True

    # noinspection PyPep8Naming
    def getRandom(self) -> int:
        rand_index = r.randint(0, len(self.element) - 1)
        return self.element[rand_index]
