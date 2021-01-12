# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:55:38 2021

@author: Caven
"""


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def subStringAtMostK(k):
            counter = defaultdict(int)
            left = 0
            ans = 0
            
            for right, num in enumerate(A):
                counter[num] +=1
                
                while len(counter) > k:
                    counter[A[left]] -=1
                    
                    if counter[A[left]] == 0:
                        del counter[A[left]]
                        
                    left +=1
                
                ans += right - left + 1
                
            
            return ans
        
        return subStringAtMostK(K) - subStringAtMostK(K-1)