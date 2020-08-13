# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 07:04:27 2020

@author: Caven
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        letter = 0
        write = 0
        
        for read, c in enumerate(chars):
            if read == n-1 or chars[read+1] != c:
                chars[write] = chars[letter]
                write +=1
                if read > letter:
                    for d in str(read-letter+1):
                        chars[write] = d
                        write +=1
                letter = read + 1

        
        return write