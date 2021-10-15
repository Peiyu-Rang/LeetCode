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


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        n = len(nums)
        for i in range(n):
            j, k = i+1, len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    # if (i,j,k) works, then (i,j,k), (i,j,k-1),..., 
                    # (i,j,j+1) all work, totally (k-j) triplets
                    count += k-j
                    j += 1
                else:
                    k -= 1
        return count
        