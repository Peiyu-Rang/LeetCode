class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPali(i,j):
            return all([s[k] == s[j-k+i] for k in range(i,j)])
        
        n = len(s)
        
        for i in range(n//2):
            if s[i]!= s[~i]:
                j = n-i-1
                return isPali(i+1,j) or isPali(i,j-1)
        return True