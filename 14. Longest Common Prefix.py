# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:08:35 2018

@author: rpy
"""

#14. Longest Common Prefix
#https://leetcode.com/problems/longest-common-prefix/
#
#Write a function to find the longest common prefix string amongst an array of strings.
#
#If there is no common prefix, return an empty string "".
#
#Example 1:
#
#Input: ["flower","flow","flight"]
#Output: "fl"
#Example 2:
#
#Input: ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
#Note:
#
#All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        prefix = strs[0] # common prefix is the first string
        
        if prefix == '':
            return ''
        
        if len(strs) == 1:
            return prefix
        
        for i in range(1, len(strs)):
            for j in range(len(prefix), -1,-1):
                if prefix[:j] == strs[i][:j]:
                    prefix = prefix[:j]
                    break
        if j ==0:
            return ''
        else:
            return prefix
        