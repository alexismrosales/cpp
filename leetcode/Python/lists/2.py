# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        val1 = self.getNumbers(l1)
        val2 = self.getNumbers(l2)
        return self.appendNumber(val1 + val2)

    def getNumbers(self, l):
        numbersStr = ""
        while l:
            numbersStr += str(l.val)
            l = l.next
        return int(numbersStr[::-1])

    def appendNumber(self, numbers):
        numbers = str(numbers)[::-1]
        head = ListNode(int(numbers[0]))
        tmp = head
        for i in range(1, len(numbers)):
            new_node = ListNode(int(numbers[i]))
            tmp.next = new_node
            tmp = tmp.next
        return head
