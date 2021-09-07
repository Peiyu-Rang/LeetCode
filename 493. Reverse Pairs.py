# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:36:02 2021

@author: Caven
"""


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [[v, i] for i,v in enumerate(nums)]
        res = 0
        
        def merge_sort(arr, left, right):
            if right - left < 2:
                return
            mid = (left + right)//2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid, right)
            merge(arr, left, right, mid)
            
        def merge(arr, left, right, mid):
            lp = left
            rp = mid
            ans = []
            nonlocal res
            
            
            # this is the additional step added to MergeSort
            while lp < mid or rp < right:
                if lp < mid and rp < right:
                    if arr[lp][0] > 2* arr[rp][0] and arr[lp][1] < arr[rp][1]:
                        res += mid - lp
                        rp +=1
                    else:
                        lp +=1
                elif lp < mid:
                    lp +=1
                else:
                    rp +=1
                    
            lp = left
            rp = mid       
            
            while lp < mid or rp < right:
                if lp < mid and rp < right:
                    if arr[lp][0] < arr[rp][0]:
                        ans.append(arr[lp])
                        lp +=1
                    else:
                        ans.append(arr[rp])
                        rp+=1
                elif lp < mid:
                    ans.append(arr[lp])
                    lp +=1
                else:
                    ans.append(arr[rp])
                    rp+=1
                        
            for i in range(left, right):
                arr[i] = ans[i-left]
        
        merge_sort(arr, 0, n)
        return res