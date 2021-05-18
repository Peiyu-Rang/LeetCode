# -*- coding: utf-8 -*-
"""
Created on Mon May 17 19:38:18 2021

@author: Caven
"""


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dic = {}
        for word in dictionary:
            if len(word) <= 2:
                w_s = word
            else:
                w_s = word[0] + str(len(word) - 2) + word[-1]
            
            if w_s not in self.dic:
                self.dic[w_s] = [word]
            elif word in self.dic[w_s]:
                continue
            else:
                self.dic[w_s].append(word)
        

    def isUnique(self, word: str) -> bool:
        if len(word) <= 2:
                w_s = word
        else:
            w_s = word[0] + str(len(word) - 2) + word[-1]
                
        if w_s not in self.dic:
            return True
        elif len(self.dic[w_s]) > 1:
            return False
        elif self.dic[w_s][0] == word:
            return True
        else:
            return False
            
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)