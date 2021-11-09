# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 20:44:01 2021

@author: Caven
"""


class SnapshotArray:

    def __init__(self, length: int):
        self.A = [[[-1, 0]] for i in range(length)]
        self.snap_id = 0
        

    def set(self, index: int, val: int) -> None:
        self.A[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
        return self.A[index][i][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
