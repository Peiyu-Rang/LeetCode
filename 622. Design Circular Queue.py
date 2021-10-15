# -*- coding: utf-8 -*-
"""
Created on Mon May 17 22:29:27 2021

@author: Caven
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.head = 0
        self.tail = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        else:
            self.queue[self.tail % self.capacity] = value
            self.tail +=1
            self.count +=1
            return True
        
        

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        else:
            self.head +=1
            self.count -=1
            return True
        

    def Front(self) -> int:
        if self.count ==0:
            return -1
        else:
            return self.queue[self.head % self.capacity]
        

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        else:
            return self.queue[(self.tail - 1) % self.capacity]
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
        
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = deque([])

    def enQueue(self, value: int) -> bool:
        if len(self.q) < self.k:
            self.q.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q:
            self.q.popleft()
            return True
        else:
            return False        

    def Front(self) -> int:
        if self.q:
            return self.q[0]
        else:
            return -1

    def Rear(self) -> int:
        if self.q:
            return self.q[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return len(self.q) == 0
        

    def isFull(self) -> bool:
        return len(self.q) == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()