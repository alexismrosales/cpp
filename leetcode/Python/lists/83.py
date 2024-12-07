from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        while tmp is not None and tmp.next is not None:
            tmpVal = tmp.val
            # if duplicate just jump to the next to next node
            if tmpVal == tmp.next.val:
                tmp.next = tmp.next.next
            # else go to next node
            else:
                tmp = tmp.next
        return head
