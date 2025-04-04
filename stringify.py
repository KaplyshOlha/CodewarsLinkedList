class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


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

print(stringify(Node(1, Node(None, Node(3)))))
