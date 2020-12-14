class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''
        
        tDic = {}
        for i in t:
            tDic[i] = tDic.get(i, 0) + 1
            
        filteredS = []
        for i, c in enumerate(s):
            if c in tDic:
                filteredS.append((i,c))
                
        left = 0
        right = 0
        required = len(tDic)
        requiredMet = 0
        candidateCount = {}
        ans = (float('inf'),None,None)
        
        while(right < len(filteredS)):
            c = filteredS[right][1]
            candidateCount[c] = candidateCount.get(c,0)+1
            
            if candidateCount[c] == tDic[c]:
                requiredMet +=1
            
            while(left <= right and requiredMet == required):
                c = filteredS[left][1]
                start = filteredS[left][0]
                end = filteredS[right][0]
                
                if end - start + 1 < ans[0]:
                    ans = (end-start+1, start, end)
                
                candidateCount[c] -=1
                if candidateCount[c] < tDic[c]:
                    requiredMet -=1
                left +=1
            
            right +=1
            
        return '' if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]