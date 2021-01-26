class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = {}
        for n in nums1:
            if n not in dic1:
                dic1[n] = 0
            dic1[n] +=1
        
        res = []
        for n in nums2:
            if n in dic1:
                if dic1[n] == 1:
                    res.append(n)
                    del dic1[n]
                else:
                    res.append(n)
                    dic1[n] -=1
            else:
                continue
        
        return res
