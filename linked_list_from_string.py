class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linked_list_from_string(s: str):
    if s == "None":
        return None
    lst = s.split(" -> ")
    _ = lst.pop()
    next = None
    while lst:
        data = lst.pop()
        next = Node(int(data), next)
    return next
