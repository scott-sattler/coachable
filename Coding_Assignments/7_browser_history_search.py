from __future__ import annotations


class Node:
    def __init__(self, val=None, prev=None, next=None) -> None:  # noqa: sbin
        self.val: str = val
        self.prev: Node = prev
        self.next: Node = next


class BrowserHistory:
    # Initializes browser history from new tab.
    # By default, the starting URL will be an empty string.
    def __init__(self) -> None:
        self.head = Node("")
        self.current = self.head

    # Returns the url of the current page.
    def current_page(self) -> str:
        return self.current.val

    # Navigates to the "page" from the current page.
    # Navigating forward should overwrite all previous forward browser history.
    def go_to(self, page: str) -> None:
        # insert new node as next (unlink subsequent nodes)
        # update head
        new_node = Node(page)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = self.current.next

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


history = BrowserHistory()
history.go_to("leetcode.com")
history.go_to("google.com")  # You are in "leetcode.com". Visit "google.com"
history.go_to("facebook.com")  # You are in "google.com". Visit "facebook.com"
history.go_to("youtube.com")  # You are in "facebook.com". Visit "youtube.com"
history.go_back()  # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
history.go_back()  # You are in "facebook.com", move back to "google.com" return "google.com"
history.go_forward()  # You are in "google.com", move forward to "facebook.com" return "facebook.com"
history.go_to("linkedin.com")  # You are in "facebook.com". Visit "linkedin.com"
history.skip_forward(2)  # You are in "linkedin.com", you cannot move forward any steps.
history.skip_backward(2)  # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
history.skip_backward(7)  # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
