# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 22:48:42 2021

@author: Caven
"""


class SparseVector:
    def __init__(self, nums: List[int]):
        self.sv = nums
        self.nonZeroIdx = set()
        for i,v in enumerate(nums):
            if v != 0:
                self.nonZeroIdx.add(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        bothNoneZero = self.nonZeroIdx.intersection(vec.nonZeroIdx)
        
        ans = 0
        for i in bothNoneZero:
            ans += self.sv[i] * vec.sv[i]
            
        return ans
        
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
        
    
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonZeros = {}
        self.nonZerosIdx = set()
        for i,v in enumerate(nums):
            if v!= 0:
                self.nonZeros[i] = v
                self.nonZerosIdx.add(i)
                

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        interset = self.nonZerosIdx.intersection(vec.nonZerosIdx)
        
        res = 0
        for i in interset:
            res += self.nonZeros[i] * vec.nonZeros[i]
            
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)