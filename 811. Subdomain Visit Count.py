# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:16:49 2020

@author: Caven
"""

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for cp in cpdomains:
            visit, domain = cp.split(' ',2)
            domainSplit = domain.split('.')
            n = len(domainSplit)
            domainSplitNames = []
            for i in range(n):
                domainSplitNames.append('.'.join(domainSplit[i:n]))
                
            for d in domainSplitNames:
                if d in dic:
                    dic[d] += int(visit)
                else:
                    dic[d] = int(visit)
                
        ans = []
        for key in dic:
            ans.append(' '.join([str(dic[key]), key]))
            
        return ans
        