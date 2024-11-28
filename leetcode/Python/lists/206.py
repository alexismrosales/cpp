# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, current):
        previous = None
        while current is not None:
            nextn = current.next
            current.next = previous
            previous = current
            current = nextn
        return previous
