# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:27:04 2021

@author: Caven
"""


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect.bisect(letters, target)
        print(idx)
        return letters[idx %len(letters)]
        