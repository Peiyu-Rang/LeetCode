# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 16:27:57 2021

@author: Caven
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wn = len(word)
        an = len(abbr)
        
        wp = 0
        ap = 0
        
        while wp < wn and ap < an:
            if abbr[ap].isalpha() or abbr[ap] == '0':
                if word[wp] != abbr[ap]:
                    return False
                else:
                    ap +=1
                    wp +=1
            else:
                count = ''
                while ap < an and abbr[ap].isnumeric():
                    count += abbr[ap]
                    ap +=1
                
                wp += int(count)
        
        if wp != wn or ap != an:
            return False
        else:
            return True
                    
                