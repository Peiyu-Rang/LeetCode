# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:57:24 2021

@author: Caven
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        total = 0
        sign = 1
        seen_sign = False
        seen_num = False
        while i < n:
            if not seen_num and not seen_sign and (s[i] == ' '):
                seen_num = False
                i +=1
                continue
            if not seen_num and not seen_sign and s[i] == '-':
                sign = -1
                seen_sign = True
                i +=1
                continue
            if not seen_num and not seen_sign and s[i] == '+':
                seen_sign = True
                i +=1
                continue
            if s[i].isnumeric():
                seen_num = True
                total = total * 10 + int(s[i])
                i +=1
                continue
            else:
                break
                
        print(total)
                
        final_total = total * sign
        if final_total < -2147483648:
            return -2147483648
        elif final_total > 2147483647:
            return 2147483647
        else:
            return final_total
        
        
class Solution:
    def myAtoi(self, s: str) -> int:
        sign=1
        s=s.strip()
        ans=0
        i=0
        if not s:
            return 0
        if s[0]=="-":
            sign=-1
            i+=1
        elif s[0]=="+":
            i+=1
        while i<len(s):
            d=ord(s[i])-ord('0')
            if d>=0 and d<=9:
                ans=(ans*10)+d
            else:
                break
            i+=1
        if ans*sign<-2**31:
            return -2**31
        elif ans*sign>(2**31)-1:
            return (2**31)-1
        return ans*sign