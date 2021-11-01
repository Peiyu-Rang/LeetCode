# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 22:49:35 2021

@author: Caven
"""


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name
                
        seen = set()
        res =[]
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                
                res.append([em_to_name[email]] + sorted(component))
                
        return res
    
    
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        p = list(range(10001))
        
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            
            return p[x]
        
        def union(x, y):
            p[find(x)] = find(y)
            
        em_to_name = {}
        em_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i +=1
                
                union(em_to_id[acc[1]], em_to_id[email])
                
        res = collections.defaultdict(list)
        
        for email in em_to_name:
            res[find(em_to_id[email])].append(email)
            
        return [[em_to_name[v[0]]] + sorted(v) for v in res.values()]
            