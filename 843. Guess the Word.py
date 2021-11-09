# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 21:45:57 2021

@author: Caven
"""


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        random.shuffle(wordlist)
        for i in range(10):
            guess = random.choice(wordlist)
            x = master.guess(guess)
            wordlist = [w for w in wordlist if sum(i == j for i, j in zip(guess, w)) == x]