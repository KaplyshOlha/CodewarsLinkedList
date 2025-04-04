class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def push(head, data):
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    node = Node(3)
    node = push(node, 2)
    node = push(node, 1)
    return node

chained = None
chained = push(chained, 3)
chained = push(chained, 2)
chained = push(chained, 1)
print(push(chained, 8) == Node(8, Node(1, Node(2, Node(3, None)))))