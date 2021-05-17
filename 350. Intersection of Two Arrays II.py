class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        
        res = []
        for key in counter1:
            if key in counter2:
                res += [key] * min(counter1[key], counter2[key])
                
        return res