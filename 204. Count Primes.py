# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:12:08 2020

@author: Caven
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
        
        return sum(primes)