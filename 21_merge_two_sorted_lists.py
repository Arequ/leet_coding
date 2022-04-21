class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1 = None, list = None -> None:
        if list1 == None or list2 == None:
            if list1:
                return list1
            elif list2:
                return list2
        fake_head = ListNode()
        current = fake_head
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        if p1:
            current.next = p1
        elif p2:
            current.next = p2
        return fake_head.next