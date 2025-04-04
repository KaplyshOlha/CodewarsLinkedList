class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if index < 0:
        raise IndexError
    for _ in range(index):
        if node:
            node = node.next
        else:
            raise IndexError
    if node:
        return node
    raise IndexError

print(get_nth(Node(1, Node(2, None)), 2))
