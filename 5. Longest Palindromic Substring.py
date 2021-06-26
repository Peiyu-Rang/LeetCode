# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:48:36 2020

@author: Caven
"""
class Solution:
    def longestPalindrome(s: str) -> str:
        n = len(s)
        if n == 0:
            return ''
        if n == 1:
            return s
        
        P = [[False for i in range(n)] for j in range(n)]
        
        
        for i in range(n):
            P[i][i] = True
            if (i+1)>(n-1):
                    continue
            P[i][i+1] = s[i] == s[i+1]
        
        def helper(i, j):
            if i == j:
                return True
            if j == i+1:
                return s[i] == s[j]
            return P[i+1][j-1] & (s[i] == s[j])
        
        for plus in range(n):
            for L in range(n):
                if L+plus > n-1:
                    continue
                P[L][L+plus] = helper(L,L+plus)
        
              
        # find the true from upper right coner
        for length in range(n-1, -1, -1):
            for L in range(n):
                R = L + length
                if R > n-1: 
                    continue
                if P[L][R]:
                    return s[L:R+1]
            
        
        
        
        
    


if __name__ == '__main__':
    s = 'esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq'
    
    res = Solution.longestPalindrome(s)

    
    print(res)
    
    
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        left = 0
        right = 0
        n = len(s)
        def expandAroundCenter(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -=1
                j +=1
            return j - i -1
        for i in range(n):
            len1 = expandAroundCenter(i, i)
            len2 = expandAroundCenter(i, i+1)
            len3 = max(len1, len2)
            
            if len3 > right - left:
                left = i - (len3-1)//2
                right = i + len3 // 2
                
            
        return s[left:right+1]