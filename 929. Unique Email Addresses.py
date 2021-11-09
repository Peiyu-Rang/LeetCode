# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 17:53:29 2021

@author: Caven
"""


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            
            res.add(local+'@' + domain)
            
        return len(res)