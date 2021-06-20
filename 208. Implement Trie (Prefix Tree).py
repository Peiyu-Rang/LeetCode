# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:10:21 2021

@author: Caven
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.trie
        for w in word:
            if w in temp:
                temp=temp[w]
            else:
                temp[w]={}
                temp=temp[w]
        temp['#'] = True
                
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self.trie
        for w in word:
            if w in temp:
                temp = temp[w]
            else:
                return False
        return '#' in temp
            
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.trie
        for w in prefix:
            if w in temp:
                temp = temp[w]
            else:
                return False
        return True
    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)