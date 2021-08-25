# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 23:39:36 2021

@author: Caven
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        if not beginWord or not endWord or not endWord in wordList:
            return []
        
        wordMap = {}
        
        for word in wordList:
            for i in range(len(word)):
                transWord = word[:i] + "*" + word[i+1:]
                if not transWord in wordMap:
                    wordMap[transWord] = []
                
                wordMap[transWord].append(word)
        
        Q = deque([(beginWord, 1, [beginWord])])
        visited = set()
        result = []
        shortestDistance = 0
        
        while(Q):
            currWord, distance, words = Q.popleft()

            visited.add(currWord)
            
            if currWord == endWord and (not shortestDistance or not (shortestDistance< distance)):
                shortestDistance = distance
                result.append(words)
                continue
            
            for i in range(len(currWord)):
                transWord = currWord[:i] + "*" + currWord[i+1:]
                
                if transWord in wordMap:
                    children = wordMap[transWord]
                    for child in children:
                        if child in visited:
                            continue
                        Q.append((child, distance+1, words+[child]))
        
        return result