def loop_size(node):
    slow = fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return 0

    count = 1
    slow = slow.next
    while slow != fast:
        slow = slow.next
        count += 1

    return count
