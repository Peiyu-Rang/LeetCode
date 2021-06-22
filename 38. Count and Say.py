# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 15:31:24 2020

@author: Caven
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        def help(s):
            n = len(s)
            i = 0
            j = 0
            count = 0
            num = s[0]
            ans = ''
            while (j < n):
                if s[i] == s[j]:
                    j +=1
                else:
                    count = j-i
                    i = j
                    ans += str(count)+num
                    if i < n:
                        num = s[i]
            count = j-i
            ans += str(count)+num
            return ans
        
        
        if n == 1:
            return '1'
        ss = '1'
        for i in range(1,n):
            ss = help(ss)
            
        return ss