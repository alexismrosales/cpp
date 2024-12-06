from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        if head.next is None:
            return head

        prev = None
        current = head
        head = head.next
        while current is not None and current.next is not None:
            next_node = current.next
            next_pair = next_node.next
            next_node.next = current
            current.next = next_pair
            if prev is not None:
                prev.next = next_node
            current.next = next_pair
            prev = current
            current = next_pair
        return head
