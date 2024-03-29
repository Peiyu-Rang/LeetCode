# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 20:18:10 2021

@author: Caven
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(i+1):
                if 0 <= i <=n and 0 <= i-j < n:
                    dp[i] = (dp[i-j] and s[i-j:i] in wordSet) or dp[i]
        print(dp)
        return dp[n]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        q = deque([0])
        seen = set()
        
        while q:
            start = q.popleft()
            
            if start in seen:
                continue
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet:
                    q.append(end)
                    if end == len(s):
                        return True
            seen.add(start)
            
        return False