# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, n):
    if not l:
        return l
    current = l
    total_count = 0
    last = None
    while current:
        last = current
        current = current.next
        total_count += 1
    if n >= total_count:
        return l
    node_pointer = 0
    target_node = total_count - n - 1
    current = l
    while node_pointer < target_node:
        current = current.next
        node_pointer += 1
    last.next = l
    new_head = current.next
    current.next = None
    return new_head