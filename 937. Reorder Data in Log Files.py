# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:38:25 2020

@author: Caven
"""

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log): # each item in the list
            iden, data = log.split(' ',1)
            if data[0].isalpha():
                return (0,data, iden)
            else:
                return (1,)
            
        return sorted(logs, key = f)

if __name__ == '__main__':
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    
    sol = Solution()
    res = sol.reorderLogFiles(logs)
    
    print(res)