# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:07:10 2018

@author: rpy
"""
#9. Palindrome Number
#https://leetcode.com/problems/palindrome-number/
#
#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
#Example 1:
#
#Input: 121
#Output: true
#Example 2:
#
#Input: -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#Example 3:
#
#Input: 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strx = str(x)
        pali = True
        for i in range(round(len(strx)/2)):
            if strx[i] == strx[-i-1]:
                continue
            else:
                return False
            
        return pali