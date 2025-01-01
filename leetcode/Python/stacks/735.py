from typing import List
class Stack:
    def __init__(self, n):
        self.stack = [n]
    def push(self, n: int):
        self.stack.append(n)
    def pop(self):
        self.stack.pop() 
    def top(self) -> int:
        return self.stack[len(self.stack)-1]
    def size(self) -> int:
        return len(self.stack)
    def isEmpty(self) -> bool:
        return len(self.stack) == 0

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = Stack(asteroids[0])
        for i  in range(1, len(asteroids)):
            asteroid = asteroids[i]
            while not s.isEmpty() and asteroid < 0 and s.top() > 0:
                    if s.top() > abs(asteroid):
                        break
                    elif s.top() < abs(asteroid):
                        s.pop()
                    else:
                        s.pop()
                        break
            else:
                s.push(asteroid)
        return s.stack
