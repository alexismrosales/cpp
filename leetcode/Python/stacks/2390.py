from typing import List


class Solution:
    def removeStars(self, s: str) -> str:
        strWithNoStart = Stack()
        for c in s:
            if c == "*":
                strWithNoStart.pop()
            else:
                strWithNoStart.push(c)
        return ''.join(strWithNoStart.stack)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, c: str) -> None:
        self.stack.append(c)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()





