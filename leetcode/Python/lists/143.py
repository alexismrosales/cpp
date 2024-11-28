class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = self.reverseList(slow.next)
        slow.next = None

        first_half = head
        while second_half:
            fh_next = first_half.next
            sh_next = second_half.next

            first_half.next = second_half
            second_half.next = fh_next

            first_half = fh_next
            second_half = sh_next

    def reverseList(self, current):
        previous = None
        while current:
            nextn = current.next
            current.next = previous
            previous = current
            current = nextn
        return previous
