
"""###########################
######## linked lists ########
###########################"""


# Definition for singly-linked list.
class ListNode:
    # Provided
    def __init__(self, val=0, next=None):  # noqa (next shadows built-in name)
        self.val = val
        self.next = next


def create_linked_list(number: list | tuple | int | str, reverse=False) -> ListNode | None:
    if isinstance(number, int) or isinstance(number, str):
        number = list(number)
    if reverse:
        number = number[::-1]
    node = ListNode()
    head = node
    for each_element in number:
        node.next = ListNode()
        node = node.next
        node.val = each_element
    return head.next


def print_linked_list(linked_list: ListNode, verbose=True) -> None:
    node = linked_list
    print_list = []
    if verbose:
        print_list = ['input order']
    while node is not None:
        print_list.append(node.val)
        node = node.next
    print(print_list)
