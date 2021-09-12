class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            return s == s[::-1]
        
        l, r = 0, len(s)-1
        
        while l < r:
            if s[l] == s[r]:
                l, r = l+1, r-1
            else:
                return is_palindrome(s[l:r]) or is_palindrome(s[l+1:r+1])
        return True
    
    
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left_deleted = False
        right_deleted = False
        n = len(s)
        
        left = 0
        right = n-1
        
        # left_delete
        while left < right:
            if s[left] != s[right]:
                if not left_deleted and not right_deleted:
                    left +=1
                    left_deleted = True
                else:
                    break
            else:
                left +=1
                right -=1
                
        if not left_deleted and not right_deleted:
            return True
        
        if left >= right:
            return True
        
        
        # right_delete:
        left = 0
        right = n-1
        
        # left_delete
        while left < right:
            if s[left] != s[right]:
                if not left_deleted or not right_deleted:
                    if not right_deleted:
                        right -=1
                        right_deleted = True
                    else:
                        break
                else:
                    return False
            else:
                left +=1
                right -=1
                
        if left >= right:
            return True
        else:
            return False
                