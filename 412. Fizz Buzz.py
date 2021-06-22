# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 21:51:09 2020

@author: Caven
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(n):
            if (i+1) % 15 == 0:
                ans.append('FizzBuzz')
            elif (i+1)%3 == 0:
                ans.append('Fizz')
            elif (i+1)%5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(i+1))
                
        return ans

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i % 15 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
                
        return res