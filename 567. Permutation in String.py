class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        
        count_s1 = {}
        for s in s1:
            if s not in count_s1:
                count_s1[s] = 0
            count_s1[s] +=1
            
        count_s2 = {}
        for i in range(n2):
            if s2[i] not in count_s2:
                count_s2[s2[i]] = 0
            count_s2[s2[i]] +=1
            if i >= n1:
                if count_s2[s2[i-n1]] == 1:
                    del count_s2[s2[i-n1]]
                else:
                    count_s2[s2[i-n1]]-=1
                    
            if count_s1 == count_s2:
                return True
        return False
