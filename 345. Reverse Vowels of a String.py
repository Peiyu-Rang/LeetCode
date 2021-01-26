class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
        n = len(s)
        if n == 0:
            return ''
        i = 0
        j = n-1
        s_list = []
        for ss in s:
            s_list.append(ss)
            
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i +=1
                j -=1
            
            if s[i] not in vowels:
                i +=1
            if s[j] not in vowels:
                j -=1
        
        res = ''
        for ss in s_list:
            res = res + ss
            
        return res
