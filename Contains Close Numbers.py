#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ContainsCloseNums(object):
    
    def __init__(self,numbers,k):
        self.numbers = numbers
        self.k = k
    def containsCloseNums(self):

        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)-1,-1,-1):
                if i != j and abs(i-j) <= self.k:
                    if self.numbers[i] == self.numbers[j]:
                        return True

        return False

