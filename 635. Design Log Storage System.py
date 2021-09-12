# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 21:56:04 2021

@author: Caven
"""


from bisect import bisect_left, bisect_right

class LogSystem:

    def __init__(self):
        self.ts = []
        self.right = ["12", "31", "23", "59", "59"]

    def put(self, id: int, timestamp: str) -> None:
        bisect.insort_right(self.ts, [timestamp, id])
        
    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        st = start.split(':')
        en = end.split(':')
        if granularity == "Year":
            st = st[:1]
            en = en[:1] + self.right
        elif granularity == "Month":
            st = st[:2]
            en = en[:2] + self.right[1:]
        elif granularity == "Day":
            st = st[:3]
            en = en[:3] + self.right[2:]
        elif granularity == "Hour":
            st = st[:4]
            en = en[:4] + self.right[3:]
        elif granularity == "Minute":
            st = st[:5]
            en = en[:5] + self.right[4:]
        start = ':'.join(st)
        end = ':'.join(en)
        lo, hi = bisect_left(self.ts, [start, 0]), bisect_right(self.ts, [end, float("inf")])
        return [id for ts, id in self.ts[lo:hi]]
