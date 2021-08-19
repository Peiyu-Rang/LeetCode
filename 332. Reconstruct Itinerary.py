# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 23:23:46 2021

@author: Caven
"""


from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from_to_dict = defaultdict(list)
        
        for ticket in tickets:
            from_to_dict[ticket[0]].append(ticket[1])
            
        for key in from_to_dict:
            from_to_dict[key] = sorted(from_to_dict[key], reverse = True)
            

        res = []
        
        
        def dfs(_from):
            _to_list = from_to_dict[_from] 
            while _to_list:
                _to = _to_list.pop()
                dfs(_to)
            res.append(_from)
            
        dfs('JFK')
        return res[::-1]
            