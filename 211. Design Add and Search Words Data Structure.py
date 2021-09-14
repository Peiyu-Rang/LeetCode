# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:31:55 2021

@author: Caven
"""


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        
        

    def addWord(self, word: str) -> None:
        curr_trie = self.trie
        for letter in word:
            if letter not in curr_trie:
                curr_trie[letter] = {}
            
            curr_trie = curr_trie[letter]
        
        curr_trie['$'] = True

    def search(self, word: str) -> bool:
        def search_in_subTrie(word, subTrie):
            for i, c in enumerate(word):
                if not c in subTrie:
                    if c == '.':
                        for x in subTrie:
                            if x != '$' and search_in_subTrie(word[i+1:], subTrie[x]):
                                return True
                    return False
                else:
                    subTrie = subTrie[c]
            
            return '$' in subTrie
        
        return search_in_subTrie(word, self.trie)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)