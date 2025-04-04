class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_pairs(head):
    if not head or not head.next:
        return head

    head_fake = Node(0)
    head_fake.next = head
    prev = head_fake

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first

    return head_fake.next