class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def reverse(head):
    if head is None or head.next is None:
        return head
    node = head.next
    result = reverse(node)
    node.next = head
    head.next = None
    return result

def stringify(node):
    if node:
        result = f"{str(node.data) if node.data else '0'} -> "
        next_node = node.next
        while next_node:
            result += f"{str(next_node.data) if next_node.data else '0'} -> "
            next_node = next_node.next
        result += "None"
    else:
        result = 'None'
    return result

print(stringify(reverse(Node(1, Node(2, Node(3, None))))))