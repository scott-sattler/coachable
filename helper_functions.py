"""###########################
######## linked lists ########
###########################"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class nAryNode:  # noqa: naming
    def __init__(self, val=None, children: list | None = None):
        self.val = val
        self.children = children


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


"""###########################
############ misc ############
###########################"""


# algorithm written in base 10
# requires base 10 input (e.g. hex unsupported)
def base_converter(from_base: int, value: int, to_base: int) -> int:
    reversed_out = []

    str_val = str(value)[::-1]
    digits = len(str_val)
    value = sum([from_base ** i * int(str_val[i]) for i in range(digits)])

    while value >= to_base:
        reversed_out.append(value % to_base)
        value //= to_base
    else:
        reversed_out.append(value)

    return int(''.join(map(str, reversed_out[::-1])))


assert base_converter(10, 256, 4) == 10000
assert base_converter(7, 256, 4) == 2023
assert base_converter(8, 1205, 3) == 212220
