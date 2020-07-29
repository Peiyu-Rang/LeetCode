# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:26:37 2020

@author: Caven
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        S = [[] for x in range(numRows)]
        count = 0
        step = -1
        for ss in s:
            S[count].append(ss)
            if (count == numRows-1) | (count == 0):
                step *= -1
            count += step
        
        res = ''
        for s in S:
            for ss in s:
                res = res+ss
        
        return res
                
        
        
        

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRowss = 3
    
    solution = Solution()
    res = solution.convert(s, numRowss)
    
    print(res)