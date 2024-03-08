'''
hash map:
    O(1) lookups

doubly linked list:
    O(1) add
    O(1) remove
    update = remove + add

1, 2, 3, 4, 4, 2, 4, 5, 2
3

queue
head -> 4 <-> 5 <-> 2 <- tail
        ^           ^

hash map
{key: [value, node]}

'''


class ListNode:
    def __init__(self, key, pre=None, nxt=None):
        self.key = key
        self.pre = pre
        self.nxt = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        self.hmap = dict()

        self.head = ListNode(None)
        self.tail = ListNode(None, self.head)
        self.head.nxt = self.tail

    def _remove_node(self, node):
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre

    def _append_node(self, node):
        node.pre = self.tail.pre
        node.nxt = self.tail
        node.pre.nxt = node
        node.nxt.pre = node

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1

        # update least recently used
        node = self.hmap[key][1]
        self._remove_node(node)
        self._append_node(node)

        value = self.hmap[key][0]
        return value

    def put(self, key: int, value: int) -> None:
        # update existing kv pair
        if key in self.hmap:
            self.hmap[key][0] = value

            node = self.hmap[key][1]
            self._remove_node(node)
            self._append_node(node)
            return None

        # add new kv pair
        self.size += 1
        if self.size > self.capacity:
            # evict LRU data
            evict_node = self.head.nxt
            self._remove_node(evict_node)
            del self.hmap[evict_node.key]

        # add node to dll
        new_node = ListNode(key)
        self._append_node(new_node)
        # add node to hash map
        self.hmap[key] = [value, new_node]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
