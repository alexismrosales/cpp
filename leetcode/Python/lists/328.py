# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if head and head.next and not head.next.next:
            return head
        last = head
        while last and last.next:
            last = last.next
        index = 1
        prev = None
        temp = head
        origin_last = last
        while temp and temp != origin_last: 
            if index % 2 == 0:    
                # Link prev with the other odd number
                current = temp
                if prev:
                    prev.next = temp.next
                # Moving temp
                temp = temp.next
                # Link current at the end of the list
                if last:
                    last.next = current
                last = current
                current.next = None
            else:
                prev = temp
                temp = temp.next
            index+=1

        # Check for last node
        if index % 2 == 0 and temp:
            if prev:
                prev.next = temp.next  
            if last:
                last.next = temp
            last = temp
            last.next = None
        return head
