# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 23:00:41 2021

@author: Caven
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        
        n1 = len(v1_list)
        n2 = len(v2_list)
        
        i = 0
        
        while i < n1 or i < n2:
            if i < n1 and i < n2:
                if int(v1_list[i]) < int(v2_list[i]):
                    return -1
                elif int(v1_list[i]) > int(v2_list[i]):
                    return 1
                else:
                    i +=1
            
            elif i < n1:
                if int(v1_list[i]) < 0:
                    return -1
                elif int(v1_list[i]) > 0:
                    return 1
                else:
                    i +=1
            else:
                if 0 < int(v2_list[i]):
                    return -1
                elif 0 > int(v2_list[i]):
                    return 1
                else:
                    i +=1
                    
        return 0