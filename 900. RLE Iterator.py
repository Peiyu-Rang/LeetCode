# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 21:21:54 2021

@author: Caven
"""


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.stack = deque(encoding)

    def next(self, n: int) -> int:
        if not self.stack:
            return -1
        if self.stack[0] >= n:
            self.stack[0] -= n
            return self.stack[1]
        else:
            n -= self.stack.popleft()
            self.stack.popleft()
            return self.next(n)
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)