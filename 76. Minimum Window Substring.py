class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        
        n = len(s)
        tDic = {}
        for i in t:
            if i in tDic:
                tDic[i] +=1
            else:
                tDic[i] = 1
        
        
        left = 0
        right = 0
        candidateCount = {}
        required = len(tDic)
        requiredMet = 0
        ans = (float('inf'), None, None)
        
        while (right < n):
            c = s[right]
            candidateCount[c] = candidateCount.get(c,0) + 1
            if c in tDic and candidateCount[c] == tDic[c]:
                requiredMet +=1
            
            while(left <= right and requiredMet == required):
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                c = s[left]
                candidateCount[c] -=1
                
                if c in tDic and candidateCount[c] < tDic[c]:
                    requiredMet -=1
                    
                left +=1
                
            right +=1
            
        return '' if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]