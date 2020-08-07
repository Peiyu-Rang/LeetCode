class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,
               'V':5,
               'X':10,
               'L':50,
               'C':100,
               'D':500,
               'M':1000}
        
        n = len(s)
        allSum = 0
        thisSum = 0
        for i in range(n-1):
            curr = dic[s[i]]
            nxt  = dic[s[i+1]]
            thisSum += curr
            if curr == nxt:
                continue
            elif curr > nxt:
                allSum +=thisSum
                thisSum = 0
            else:
                thisSum = -thisSum
        
        allSum += thisSum + dic[s[-1]]
        return allSum
            
            