# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 21:39:45 2021

@author: Caven
"""
class TweetCounts:

    def __init__(self):
        self.memo = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.memo[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        arr = sorted(self.memo[tweetName])
        dic = {"minute": 60, "hour": 3600, "day": 86400}
        ans = []
        for i in range(startTime, endTime + 1, dic[freq]):
            start_time = i
            end_time = min(endTime, i + dic[freq] - 1)
            ans += [self.bs_last(arr, end_time) + 1 - self.bs_first(arr, start_time)]
        return ans
            
    #get the index of the smallest number greater or equal to target
    def bs_first(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    #get the index of the greatest number smaller or equal to target
    def bs_last(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
        


class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        freq_map = {'minute':60,
                    'hour': 3600,
                    'day': 86400}
        self.tweets[tweetName].sort()
        
        def binarySearch_l(time): 
            n = len(self.tweets[tweetName])
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if mid == n-1:
                    if self.tweets[tweetName][mid] < time:
                        return mid + 1
                    else:
                        return 0
                    
                if self.tweets[tweetName][mid] < time and self.tweets[tweetName][mid + 1] >= time:
                    return mid + 1
                elif self.tweets[tweetName][mid] < time:
                    left = mid + 1
                elif self.tweets[tweetName][mid] >= time:
                    right = mid -1    
            return 0
        
        def binarySearch_le(time): 
            n = len(self.tweets[tweetName])
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if mid == n-1:
                    if self.tweets[tweetName][mid] <= time:
                        return mid + 1
                    else:
                        return 0
                    
                if self.tweets[tweetName][mid] <= time and self.tweets[tweetName][mid + 1] > time:
                    return mid + 1
                elif self.tweets[tweetName][mid] <= time:
                    left = mid + 1
                elif self.tweets[tweetName][mid] > time:
                    right = mid -1    
            return 0
        
        time_slots = []
        i = startTime
        while i <= endTime:
            if i + freq_map[freq]-1 <= endTime:
                time_slots.append([i, i+freq_map[freq]-1])
                i += freq_map[freq]
            else:
                time_slots.append([i, endTime])
                break
        
        res = []
        for s, e in time_slots:
            idx_s = binarySearch_l(s)
            idx_e = binarySearch_le(e)
            res.append(idx_e - idx_s)
        
        return res
        
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)