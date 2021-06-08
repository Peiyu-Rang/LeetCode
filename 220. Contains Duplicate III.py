# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 21:33:30 2021

@author: Caven
"""


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        s = sorted(list(zip(range(len(nums)), nums)), key=lambda x: x[1])
        i = 0
        j = 1
        while j < len(s):
            if s[j][1] - s[i][1] <= t:
                if abs(s[j][0]-s[i][0]) <= k:
                    return True
                else:
                    j += 1
            else:
                i += 1
                j = i + 1
        return False
    
    
    
class Solution:
    def _get_bucket_id(self, num, size):
        """
        Assume buckets are k: [k*size, ..., (k+1)*size-1] for k >= 0
            and k: [-(k+2)size+1, ..., -(k+1)*size] for k < 0.
        By convention we place num = 0 to the k=0 bucket.
        This makes sure that the range of each bucket is <= size-1.
        """
        if num >= 0:
            return num//size
        else:
            return num//size - 1
    
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        bucket = {}
        size = t + 1
        
        for i, num in enumerate(nums):
            bucket_id = self._get_bucket_id(num, size)
            if bucket_id in bucket:
                return True
            
            # check adjacent buckets
            if (bucket_id+1) in bucket and bucket[bucket_id+1] - num <= t:
                return True
            if (bucket_id-1) in bucket and num - bucket[bucket_id-1] <= t:
                return True
            
            bucket[bucket_id] = num
            # we want the indices to be at most k apart
            # so once we have added k elements in the bucket,
            # everytime we want to add a new element, 
            # we need to disregard the least recent element
            if i >= k:
                bucket.pop(self._get_bucket_id(nums[i-k], size))
        
        return False