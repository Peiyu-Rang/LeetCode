# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 21:43:45 2020

@author: Caven
"""

connections = [[0,1],[1,2],[2,0],[1,3]]
connections = set(map(tuple, (map(sorted, connections))))