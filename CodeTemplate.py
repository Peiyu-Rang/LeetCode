# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 09:50:38 2021

@author: Caven
"""


# Binary search in sorted array

#get the index of the smallest number greater or equal to target
def bs_first( arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
        
    return left

#get the index of the greatest number smaller or equal to target
def bs_last( arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return right


arr = [1, 2, 3, 3,3,3,3,3,6]
target = 10
res = bs_first(arr, target)
print(res)
