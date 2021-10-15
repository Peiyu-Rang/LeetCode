class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        
        if not s or not t:
            return ''
        if m > n:
            return ''
        
        left = 0
        right = 0
        
        counter_t = collections.Counter(t)
        requirement = len(counter_t)
        
        formed = 0
        counter_win = defaultdict(int)
        
        res = (float('inf'), 0,0)
        
        
        while right < n:
            c = s[right]
            counter_win[c] += 1
            
            if c in counter_t and counter_t[c] == counter_win[c]:
                formed +=1
            
            while left <= right and formed == requirement:
                c = s[left]
                if right - left + 1 < res[0]:
                    res = (right - left + 1, left, right)
                    
                counter_win[c] -=1
                
                if c in counter_t and counter_win[c] < counter_t[c]:
                    formed -=1
                    
                left +=1
                
            right +=1
            
        return '' if res[0] == float('inf') else s[res[1]:res[2]+1]