# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 07:09:57 2020

@author: Caven
"""

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp_dic = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        
        if message in self.timestamp_dic:
            if self.timestamp_dic[message] + 10 <= timestamp:
                self.timestamp_dic[message] = timestamp
                return True
            else:
                return False
        else:
            self.timestamp_dic[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)