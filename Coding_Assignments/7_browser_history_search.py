from __future__ import annotations

"""
Implementation Contains:
    Doubly Linked List + Hash Table
    Trie
"""

# todo: testing
"""
Testing

As usual, please write up sufficient test cases to ensure your code works on a 
variety of inputs. You do not need to test the URL navigation functions as you 
can assume they work from the previous assignment.

To start with writing test cases, imagine several inputs/outputs qualitatively. 
"What if these weird cases happened" then think about those cases and convert 
them to concrete inputs to verify your code.
Deliverables

Complete BrowserHisory with the autocomplete, clear_history functions along 
with sufficient unit tests that are labeled. 
"""


class DLLNode:
    def __init__(self, val=None, prev=None, next=None) -> None:  # noqa: sbin
        self.val: str = val
        self.prev: DLLNode = prev
        self.next: DLLNode = next


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word: bool = False


class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, string: str):
        node_pointer = self.root
        for char in string:
            if char not in node_pointer.children:
                node_pointer.children[char] = TrieNode()
            node_pointer = node_pointer.children[char]
        else:
            node_pointer.is_word = True

    def starts_with(self, prefix: str):
        node = self.root
        # traverse trie until at prefix level
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return ""

        words = self._get_words(node, prefix, list())

        return words

    def _get_words(self, node, base, words):
        if node.is_word:
            words.append(base)
        if len(node.children) > 0:
            for each_child in node.children:
                next_base = base + each_child
                self._get_words(node.children[each_child], next_base, words)
        return words


class BrowserHistory:
    # Initializes browser history from new tab.
    # By default, the starting URL will be an empty string.
    def __init__(self) -> None:
        self.head: DLLNode = DLLNode("")
        self.current: DLLNode = self.head
        self.history: dict = dict()

    # Returns the url of the current page.
    def current_page(self) -> str:
        return self.current.val

    # Navigates to the "page" from the current page.
    # Navigating forward should overwrite all previous forward browser history.
    def go_to(self, page: str) -> None:
        # remove 'overwritten' (discarded) pages
        probe = self.current
        while probe.next is not None:
            self.history[probe.val] -= 1
            probe = probe.next

        # update head
        new_node = DLLNode(page)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = self.current.next

        # add to dict
        if page in self.history:
            self.history[page] += 1
        else:
            self.history[page] = 1

    # Navigates to the previous page visited.
    # After navigating return the URL of the current page.
    def go_back(self) -> str:
        self.current = self.current.prev
        return self.current.val

    # Navigates to the page ahead in browser history.
    # If there is no page ahead, do nothing.
    # After navigating return the URL of the current page.
    def go_forward(self) -> str | None:
        if self.current.next is not None:
            self.current = self.current.next
            return self.current.val
        return None

    # Navigates backwards N pages in browser history.
    # If there are not N pages behind, then return the new tab URL which is an
    # empty string.
    # After navigating return the URL of the current page.
    def skip_backward(self, skip_number: int) -> int | str:
        # probe depth
        # navigate
        probe = self.current
        i = 0
        while i < skip_number:
            probe = probe.prev
            if probe is None:
                return ""
            i += 1
        self.current = probe
        return self.current.val

    # Navigates forward N pages in browser history.
    # If there are not N pages ahead, then go as far as you can.
    # After navigating return the URL of the current page.
    def skip_forward(self, skip_number: int) -> str:
        probe = self.current
        i = 0
        while i < skip_number:
            if probe.next is None:
                break
            probe = probe.next
            i += 1
        self.current = probe
        return self.current.val

    # Returns a list of strings that match the input prefix
    # Limit is the max number of elements that will be returned.
    # When limit is used, return the matches with the highest frequency first.
    # When limit is not used, the matches must be returned in order of
    # frequency those with the highest frequency to appear first.
    def autocomplete(self, prefix: str, limit=None) -> list[str]:
        # construct Trie
        trie = Trie()
        for each in self.history.keys():
            trie.insert(each)
        # get all prefix
        words = trie.starts_with(prefix)

        # order by frequency
        prefix_hist = {k: v for k, v in self.history.items() if k in words}
        sorted_dict = {k: v for k, v in sorted(prefix_hist.items(),
                                               key=lambda x: x[1],
                                               reverse=True)}
        # sorted_dict = {k: v for k, v in sorted(self.history.items(),
        #                                        key=lambda x: x[1],
        #                                        reverse=True) if k in words}

        return list(sorted_dict.keys())[0:limit]

    # Erases entire browser history and reverts to initial state of
    # BrowserHistory.
    def clear_history(self) -> None:
        self.__init__()


# history = BrowserHistory()
# history.go_to("leetcode.com")
# history.go_to("google.com")  # You are in "leetcode.com". Visit "google.com"
# history.go_to("facebook.com")  # You are in "google.com". Visit "facebook.com"
# history.go_to("youtube.com")  # You are in "facebook.com". Visit "youtube.com"
# history.go_back()  # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
# history.go_back()  # You are in "facebook.com", move back to "google.com" return "google.com"
# history.go_forward()  # You are in "google.com", move forward to "facebook.com" return "facebook.com"
# history.go_to("linkedin.com")  # You are in "facebook.com". Visit "linkedin.com"
# history.skip_forward(2)  # You are in "linkedin.com", you cannot move forward any steps.
# history.skip_backward(2)  # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
# history.skip_backward(7)  # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"


history = BrowserHistory()
history.go_to("leetcode.com")
history.go_to("google.com")  # You are in "leetcode.com". Visit "google.com"
history.go_to("facebook.com")  # You are in "google.com". Visit "facebook.com"
history.go_to("youtube.com")  # You are in "facebook.com". Visit "youtube.com"
history.go_back()  # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
history.go_back()  # You are in "facebook.com", move back to "google.com" return "google.com"
history.go_forward()  # You are in "google.com", move forward to "facebook.com" return "facebook.com"
history.go_to("linkedin.com")  # You are in "facebook.com". Visit "linkedin.com"
history.go_to("godaddy.com")  # You are in "linkedin.com". Visit "godaddy.com"
history.go_to("google.com")  # You are in "linkedin.com". Visit "godaddy.com"

history.go_to("google.com/foo")
history.go_to("gone.net")
history.go_to("google.com/bar")
history.go_to("gone.net")
history.go_to("google.com/foo")
history.go_to("google.com/baz")
history.go_to("google.com/baz")
history.go_to("gone.net")
history.go_to("google.com/baz")
history.go_to("google.com/foo")
history.go_to("gone.net")
history.go_to("gnat.net")
history.go_to("gosh.biz")


history.go_back()
history.skip_forward(3)  # You are in "linkedin.com", you cannot move forward any steps.
history.skip_backward(3)  # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
history.skip_backward(7)  # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

print(history.autocomplete("go", limit=None))  # You search for prefix "go" with no limit. Returns "godaddy.com" and "google.com"
print(history.autocomplete("abc", limit=None))  # You search for prefix "abc" with no limit. Returns empty list since no matches.

print(history.autocomplete("go", limit=1))  # You search for prefix "go" with no limit. Returns "google.com" because it matches "go*" and was visited the most times.

history.clear_history()
history.current_page()  # Current page is "" for new tab.
print(history.autocomplete("go"))  # You search for prefix "go". Returns empty list since history is cleared.