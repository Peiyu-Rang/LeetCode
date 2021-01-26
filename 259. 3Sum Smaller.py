class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        nums.sort()
        res = 0
        last_end = n-1
        
        for i in range(n-2):
            if 3 * nums[i] >= target:
                return res
            two_target = target - nums[i]
            j = i + 1
            while j < last_end and nums[j] + nums[last_end] >= two_target:
                last_end -=1
            k = last_end
            while j < k:
                if nums[j] + nums[k] < two_target:
                    res += k-j
                    j += 1
                else:
                    k -=1
        return res
