# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 10:49:53 2021

@author: Caven
"""


from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        N = len(beginWord)
        
        word_dict = defaultdict(list)
        for word in wordList:
            for i in range(N):
                word_dict[word[:i] + '*' + word[i+1:]].append(word)
                
        queue = deque([(beginWord, 1)])
        seen = set(beginWord)
        
        while queue:
            current_word, level = queue.popleft()
            for i in range(N):
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]
                
                for word in word_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in seen:
                        seen.add(word)
                        queue.append((word, level + 1))
                        
                word_dict[intermediate_word] = []
        return 0
                        
                    